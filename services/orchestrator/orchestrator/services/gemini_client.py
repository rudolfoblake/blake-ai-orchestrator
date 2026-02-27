import os
from typing import Dict, Any

from ..utils.http import async_post_json


async def call_gemini(prompt: str) -> str:
    """Chama a API do Google Gemini e retorna o texto gerado."""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("Missing GEMINI_API_KEY")

    url = f"https://generativelanguage.googleapis.com/v1beta/models/{os.getenv('GEMINI_MODEL', 'gemini-pro')}:generateContent?key={api_key}"
    persona = os.getenv("PERSONA_GEMINI") or os.getenv("PERSONA_DEFAULT")
    user_text = prompt if not persona else f"{persona}\n\n{prompt}"
    payload: Dict[str, Any] = {"contents": [{"parts": [{"text": user_text}]}]}
    j = await async_post_json(url, json=payload, timeout=60.0, retries=2, backoff_base=0.6)
    return j["candidates"][0]["content"]["parts"][0]["text"]
