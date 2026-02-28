import os
import asyncio
from typing import Dict, Any, List
import time
import asyncio
from asyncio import Semaphore

from .analyzer import analyze_responses
from .openai_client import call_openai
from .claude_client import call_claude
from .deepseek_client import call_deepseek
from .gemini_client import call_gemini
from ..utils.circuit import get_breaker
from ddtrace import tracer


async def infer_final_answer(prompt_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Dispara chamadas assíncronas aos provedores habilitados e agrega resultados.
    Estratégia de seleção do “best_text”: atualmente o mais longo (proxy simples).
    A “confidence” é derivada das métricas do analyzer ponderadas por pesos.
    """
    prompt = (prompt_data or {}).get("prompt", "")
    enabled = {
        s.strip().lower()
        for s in os.getenv("ENABLED_PROVIDERS", "openai,claude,deepseek,gemini").split(",")
        if s.strip()
    }

    # Semáforos por provedor para limitar concorrência
    def _limit_for(name: str) -> int:
        key = f"PROVIDER_CONCURRENCY_{name.upper()}"
        try:
            return int(os.getenv(key) or os.getenv("PROVIDER_CONCURRENCY_DEFAULT", "2"))
        except Exception:
            return 2

    semaphores: Dict[str, Semaphore] = {p: Semaphore(_limit_for(p)) for p in enabled}

    async def _run_provider(name: str):
        breaker = get_breaker(name)
        start = time.time()
        status = "ok"
        error_name = None
        text = ""
        if not breaker.allow():
            status = "skipped"
            error_name = "circuit_open"
        else:
            try:
                async with semaphores[name]:
                    with tracer.trace("provider.call", service="orchestrator", resource=name) as span:
                        span.set_tag("provider.name", name)
                        span.set_tag("prompt.length", len(prompt))
                        if name == "openai":
                            text = await call_openai(prompt)
                        elif name == "claude":
                            text = await call_claude(prompt)
                        elif name == "deepseek":
                            text = await call_deepseek(prompt)
                        elif name == "gemini":
                            text = await call_gemini(prompt)
                        span.set_tag("response.length", len(text))
                breaker.success()
            except Exception as e:
                status = "error"
                error_name = e.__class__.__name__
                breaker.fail()
        duration_ms = round((time.time() - start) * 1000.0, 2)
        try:
            span = tracer.current_span()
            if span:
                span.set_tag(f"provider.{name}.status", status)
                span.set_tag(f"provider.{name}.duration_ms", duration_ms)
                if error_name:
                    span.set_tag(f"provider.{name}.error", error_name)
        except Exception:
            pass
        return name, text if status == "ok" else ""

    coros: List[Any] = []
    if "openai" in enabled:
        coros.append(_run_provider("openai"))
    if "claude" in enabled:
        coros.append(_run_provider("claude"))
    if "deepseek" in enabled:
        coros.append(_run_provider("deepseek"))
    if "gemini" in enabled:
        coros.append(_run_provider("gemini"))

    if not coros:
        return {"final_answer": "", "confidence": 0.0, "sources": {}}

    results = await asyncio.gather(*coros, return_exceptions=True)
    responses: Dict[str, str] = {name: text for (name, text) in results}

    analysis = await analyze_responses(responses)
    weights = {
        "similarity": float(os.getenv("INFER_WEIGHT_SIMILARITY", 0.4)),
        "confidence": float(os.getenv("INFER_WEIGHT_CONFIDENCE", 0.3)),
        "context": float(os.getenv("INFER_WEIGHT_CONTEXT", 0.3)),
    }
    combined_score = sum(analysis.get(k, 0.0) * w for k, w in weights.items())
    best_text = max(responses.values(), key=len, default="")

    return {"final_answer": best_text, "confidence": round(combined_score, 2), "sources": responses}
