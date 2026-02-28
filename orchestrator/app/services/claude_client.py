import os
from typing import List, Dict, Any

from ..utils.http import async_post_json


async def call_claude(prompt: str) -> str:
    """Chama a API da Anthropic (Claude) e retorna o texto da mensagem."""
    api_key = os.getenv("CLAUDE_API_KEY")
    if not api_key:
        raise RuntimeError("Missing CLAUDE_API_KEY")

    url = "https://api.anthropic.com/v1/messages"
    headers: Dict[str, str] = {
        "x-api-key": api_key,
        "anthropic-version": os.getenv("ANTHROPIC_VERSION", "2023-06-01"),
        "content-type": "application/json",
    }
    max_tokens = int(os.getenv("MAX_TOKENS", 512))
    persona = os.getenv("PERSONA_CLAUDE") or os.getenv("PERSONA_DEFAULT")

    messages: List[Dict[str, Any]] = []
    if persona:
        messages.append({"role": "system", "content": persona})
    messages.append({"role": "user", "content": prompt})

    data: Dict[str, Any] = {
        "model": os.getenv("CLAUDE_MODEL", "claude-3-opus-20240229"),
        "max_tokens": max_tokens,
        "messages": messages,
    }
    j = await async_post_json(url, headers=headers, json=data, timeout=60.0, retries=2, backoff_base=0.6)
    # anthropic retorna conteúdo como array com campos de texto
    return j["content"][0]["text"]
