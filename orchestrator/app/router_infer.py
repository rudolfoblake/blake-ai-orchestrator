import asyncio
import json
import time
import os
from typing import Dict, Any

from fastapi import APIRouter
from pydantic import BaseModel, Field

# v4.0 pipeline delega para services.inferencer
from .services.inferencer import infer_final_answer
from database.db import InferenceLog, get_session
from .utils.crypto import encrypt_if_configured
from .utils.cache import cache_get, cache_set
from .utils.logging import log_info


class PromptRequest(BaseModel):
    """Modelo de entrada da API /infer."""
    prompt: str = Field(..., min_length=1, description="Texto de entrada para inferência")


class InferenceResponse(BaseModel):
    """Modelo de saída da API /infer."""
    final_answer: str
    confidence: float
    sources: Dict[str, str]


router = APIRouter()


@router.post("/", response_model=InferenceResponse)
async def infer(body: PromptRequest) -> InferenceResponse:
    """Realiza a orquestração entre provedores e retorna a melhor resposta."""
    p = body.prompt.strip()
    if not p:
        return InferenceResponse(final_answer="", confidence=0.0, sources={})

    start = time.time()

    # Cache opcional via Redis utilitário
    cache_key = f"infer:{p}"
    cached = cache_get(cache_key)
    if cached:
        try:
            raw = cached.decode("utf-8") if isinstance(cached, (bytes, bytearray)) else cached
            data = json.loads(raw)
            return InferenceResponse(**data)
        except Exception:
            pass

    # Orquestra a inferência
    result: Dict[str, Any] = await infer_final_answer({"prompt": p})

    # Redação/Criptografia (preferir criptografia quando configurada)
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

    # Persistência do log de inferência (best-effort)
    try:
        with get_session() as session:
            outputs_for_db = (
                sources_for_log if encryption_enabled else json.dumps(sources_for_log)
            )
            log = InferenceLog(
                prompt=prompt_for_log,
                outputs=outputs_for_db,
                final_response=final_for_log,
            )
            session.add(log)
            session.commit()
    except Exception:
        # Manter a API saudável mesmo com falhas no DB
        pass

    # Cache do resultado (TTL configurável, padrão 60s)
    try:
        ttl = int(os.getenv("CACHE_TTL", "60"))
    except Exception:
        ttl = 60
    try:
        cache_set(cache_key, json.dumps(result), ttl=ttl)
    except Exception:
        pass

    log_info("infer concluído")
    return InferenceResponse(**result)


@router.post("", response_model=InferenceResponse)
async def infer_no_slash(body: PromptRequest) -> InferenceResponse:
    """Compatibilidade: aceita POST em /infer (sem barra)."""
    return await infer(body)
