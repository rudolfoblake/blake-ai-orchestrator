import asyncio
import json
import time
import os

from fastapi import APIRouter

# v4.0 pipeline delegates to services.inferencer
from .services.inferencer import infer_final_answer
from database.db import InferenceLog, get_session
from .utils.monitoring import send_event as send_monitor_event
from .utils.crypto import encrypt_if_configured

try:
    import redis
except ImportError:
    redis = None


router = APIRouter()


@router.post("/")
async def infer(prompt: dict):
    p = (prompt or {}).get("prompt", "")
    if not p.strip():
        return {"final_answer": "", "confidence": 0.0, "sources": {}}

    start = time.time()

    # Optional cache via Redis
    cache_key = f"infer:{p.strip()}"
    cached = None
    r = None
    if redis:
        try:
            redis_url = os.getenv("REDIS_URL", "redis://redis:6379")
            r = redis.from_url(redis_url)
            cached = r.get(cache_key)
        except Exception:
            r = None
            cached = None

    if cached:
        data = json.loads(cached)
        return data

    # v4.0: get final answer via inferencer service
    result = await infer_final_answer({"prompt": p})

    # Redaction or encryption (prefer encryption if configured)
    encryption_enabled = bool(os.getenv("LOG_ENCRYPTION_KEY", "").strip())
    redact = os.getenv("REDACT_PROMPTS", "true").lower() in ("1", "true", "yes")
    if encryption_enabled:
        prompt_for_log = encrypt_if_configured(p)
        final_for_log = encrypt_if_configured(result.get("final_answer", ""))
        sources_for_log = encrypt_if_configured(json.dumps(result.get("sources", {})))
    else:
        prompt_for_log = "[redacted]" if redact else p
        final_for_log = "[redacted]" if redact else result.get("final_answer", "")
        sources_for_log = {} if redact else result.get("sources", {})

    # Persist inference log (best-effort)
    try:
        with get_session() as session:
            # If encryption is enabled, 'outputs_for_db' is already a string ciphertext.
            outputs_for_db = (
                sources_for_log
                if encryption_enabled
                else json.dumps(sources_for_log)
            )
            log = InferenceLog(
                prompt=prompt_for_log,
                outputs=outputs_for_db,
                final_response=final_for_log,
            )
            session.add(log)
            session.commit()
    except Exception:
        # Swallow DB errors to keep endpoint healthy
        pass

    # Send monitoring event (best-effort, non-blocking)
    try:
        payload = {
            "prompt": prompt_for_log,
            "final_answer": final_for_log,
            "confidence": result.get("confidence"),
            "sources": sources_for_log,
            "duration_ms": round((time.time() - start) * 1000, 2),
        }
        asyncio.create_task(asyncio.to_thread(send_monitor_event, payload))
    except Exception:
        pass

    # Cache result for 60s
    if r:
        try:
            r.setex(cache_key, 60, json.dumps(result))
        except Exception:
            pass

    return result