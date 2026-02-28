import os
from typing import List, Dict, Any

from ..utils.http import async_post_json


async def call_openai(prompt: str) -> str:
    """Chama a API da OpenAI e retorna o conteúdo de texto da resposta."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("Missing OPENAI_API_KEY")

    url = "https://api.openai.com/v1/chat/completions"
    headers: Dict[str, str] = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    temperature = float(os.getenv("TEMPERATURE", 0.7))
    max_tokens = int(os.getenv("MAX_TOKENS", 512))
    persona = os.getenv("PERSONA_OPENAI") or os.getenv("PERSONA_DEFAULT")

    messages: List[Dict[str, Any]] = []
    if persona:
        messages.append({"role": "system", "content": persona})
    messages.append({"role": "user", "content": prompt})

    data: Dict[str, Any] = {
        "model": os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
    }
    j = await async_post_json(url, headers=headers, json=data, timeout=60.0, retries=2, backoff_base=0.6)
    return j["choices"][0]["message"]["content"]
