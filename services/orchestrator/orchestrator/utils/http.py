"""
Utilitários HTTP assíncronos com retry/backoff.
Evita duplicação de lógica de resiliência nos clients de provedores.
"""
from __future__ import annotations

import asyncio
import random
from typing import Any, Dict, Optional

import httpx


async def async_post_json(
    url: str,
    *,
    headers: Optional[Dict[str, str]] = None,
    json: Optional[Dict[str, Any]] = None,
    timeout: float = 60.0,
    retries: int = 3,
    backoff_base: float = 0.5,
) -> Dict[str, Any]:
    """
    Executa POST JSON com tentativas e backoff exponencial com jitter.
    - retries: número máximo de novas tentativas em caso de erro/transiente.
    - backoff_base: base do tempo de espera (ex.: 0.5s, 1.0s).
    """
    attempt = 0
    last_err: Exception | None = None
    async with httpx.AsyncClient(timeout=timeout) as client:
        while attempt <= retries:
            try:
                r = await client.post(url, headers=headers, json=json)
                r.raise_for_status()
                return r.json()
            except Exception as e:
                last_err = e
                if attempt == retries:
                    break
                delay = (2 ** attempt) * backoff_base
                delay = delay * (0.8 + 0.4 * random.random())  # jitter
                await asyncio.sleep(delay)
                attempt += 1
    assert last_err is not None
    raise last_err
