import os
import httpx


async def call_claude(prompt: str) -> str:
    api_key = os.getenv("CLAUDE_API_KEY")
    if not api_key:
        raise RuntimeError("Missing CLAUDE_API_KEY")

    url = "https://api.anthropic.com/v1/messages"
    headers = {
        "x-api-key": api_key,
        "anthropic-version": os.getenv("ANTHROPIC_VERSION", "2023-06-01"),
        "content-type": "application/json",
    }
    max_tokens = int(os.getenv("MAX_TOKENS", 512))
    persona = os.getenv("PERSONA_CLAUDE") or os.getenv("PERSONA_DEFAULT")

    messages = []
    if persona:
        messages.append({"role": "system", "content": persona})
    messages.append({"role": "user", "content": prompt})

    data = {
        "model": os.getenv("CLAUDE_MODEL", "claude-3-opus-20240229"),
        "max_tokens": max_tokens,
        "messages": messages,
    }
    async with httpx.AsyncClient(timeout=60) as client:
        r = await client.post(url, headers=headers, json=data)
        r.raise_for_status()
        j = r.json()
        # anthropic returns content array with text fields
        return j["content"][0]["text"]