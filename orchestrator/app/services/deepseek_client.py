import os
from typing import List, Dict, Any

from ..utils.http import async_post_json


async def call_deepseek(prompt: str) -> str:
    """Chama a API da DeepSeek e retorna o conteúdo textual."""
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        raise RuntimeError("Missing DEEPSEEK_API_KEY")

    url = "https://api.deepseek.com/chat/completions"
    headers: Dict[str, str] = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    persona = os.getenv("PERSONA_DEEPSEEK") or os.getenv("PERSONA_DEFAULT")

    messages: List[Dict[str, Any]] = []
    if persona:
        messages.append({"role": "system", "content": persona})
    messages.append({"role": "user", "content": prompt})

    data: Dict[str, Any] = {"model": os.getenv("DEEPSEEK_MODEL", "deepseek-chat"), "messages": messages}
    j = await async_post_json(url, headers=headers, json=data, timeout=60.0, retries=2, backoff_base=0.6)
    return j["choices"][0]["message"]["content"]
