import os
import asyncio

from .analyzer import analyze_responses
from .openai_client import call_openai
from .claude_client import call_claude
from .deepseek_client import call_deepseek
from .gemini_client import call_gemini


async def infer_final_answer(prompt_data: dict):
    prompt = (prompt_data or {}).get("prompt", "")
    enabled = {s.strip().lower() for s in os.getenv("ENABLED_PROVIDERS", "openai,claude,deepseek,gemini").split(",") if s.strip()}

    tasks = []
    names = []
    if "openai" in enabled:
        tasks.append(call_openai(prompt))
        names.append("openai")
    if "claude" in enabled:
        tasks.append(call_claude(prompt))
        names.append("claude")
    if "deepseek" in enabled:
        tasks.append(call_deepseek(prompt))
        names.append("deepseek")
    if "gemini" in enabled:
        tasks.append(call_gemini(prompt))
        names.append("gemini")

    if not tasks:
        return {"final_answer": "", "confidence": 0.0, "sources": {}}

    results = await asyncio.gather(*tasks, return_exceptions=True)
    responses = {}
    for name, res in zip(names, results):
        responses[name] = res if not isinstance(res, Exception) else ""

    analysis = await analyze_responses(responses)
    weights = {
        "similarity": float(os.getenv("INFER_WEIGHT_SIMILARITY", 0.4)),
        "confidence": float(os.getenv("INFER_WEIGHT_CONFIDENCE", 0.3)),
        "context": float(os.getenv("INFER_WEIGHT_CONTEXT", 0.3)),
    }
    combined_score = sum(analysis.get(k, 0.0) * w for k, w in weights.items())
    best_text = max(responses.values(), key=len, default="")

    return {"final_answer": best_text, "confidence": round(combined_score, 2), "sources": responses}