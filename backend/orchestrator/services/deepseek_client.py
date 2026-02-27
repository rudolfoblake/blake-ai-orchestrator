import os
import httpx


async def call_deepseek(prompt: str) -> str:
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        raise RuntimeError("Missing DEEPSEEK_API_KEY")

    url = "https://api.deepseek.com/chat/completions"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    persona = os.getenv("PERSONA_DEEPSEEK") or os.getenv("PERSONA_DEFAULT")

    messages = []
    if persona:
        messages.append({"role": "system", "content": persona})
    messages.append({"role": "user", "content": prompt})

    data = {"model": os.getenv("DEEPSEEK_MODEL", "deepseek-chat"), "messages": messages}
    async with httpx.AsyncClient(timeout=60) as client:
        r = await client.post(url, headers=headers, json=data)
        r.raise_for_status()
        j = r.json()
        return j["choices"][0]["message"]["content"]