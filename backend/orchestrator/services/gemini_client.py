import os
import httpx


async def call_gemini(prompt: str) -> str:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("Missing GEMINI_API_KEY")

    url = f"https://generativelanguage.googleapis.com/v1beta/models/{os.getenv('GEMINI_MODEL', 'gemini-pro')}:generateContent?key={api_key}"
    persona = os.getenv("PERSONA_GEMINI") or os.getenv("PERSONA_DEFAULT")
    user_text = prompt if not persona else f"{persona}\n\n{prompt}"
    payload = {"contents": [{"parts": [{"text": user_text}]}]}
    async with httpx.AsyncClient(timeout=60) as client:
        r = await client.post(url, json=payload)
        r.raise_for_status()
        j = r.json()
        return j["candidates"][0]["content"]["parts"][0]["text"]