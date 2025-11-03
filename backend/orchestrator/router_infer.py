import asyncio
import json
import time

from fastapi import APIRouter

# v4.0 pipeline delegates to services.inferencer
from .services.inferencer import infer_final_answer
from database.db import InferenceLog, get_session
from .utils.monitoring import send_event as send_monitor_event

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
            r = redis.Redis(host="redis", port=6379, db=0)
            cached = r.get(cache_key)
        except Exception:
            r = None
            cached = None

    if cached:
        data = json.loads(cached)
        return data

    # v4.0: get final answer via inferencer service
    result = await infer_final_answer({"prompt": p})

    # Persist inference log (best-effort)
    try:
        with get_session() as session:
            log = InferenceLog(
                prompt=p,
                outputs=json.dumps(result.get("sources", {})),
                final_response=result.get("final_answer", ""),
            )
            session.add(log)
            session.commit()
    except Exception:
        # Swallow DB errors to keep endpoint healthy
        pass

    # Envia evento de monitoramento (best-effort, não bloqueante)
    try:
        payload = {
            "prompt": p,
            "final_answer": result.get("final_answer"),
            "confidence": result.get("confidence"),
            "sources": result.get("sources", {}),
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