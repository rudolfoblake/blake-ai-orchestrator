"""
Analisador de respostas dos provedores.

Realiza análise de similaridade simples via overlap de tokens (Jaccard).
Dependências pesadas de ML foram removidas para otimizar o orchestrator.
"""
from typing import Dict, List


async def analyze_responses(responses: Dict[str, str]) -> Dict[str, float]:
    """
    Calcula métricas de similaridade/“confiança”/“contexto” entre respostas.
    Usa overlap de tokens (Jaccard) como métrica leve e eficiente.
    """
    texts: List[str] = [t or "" for t in responses.values()]

    # Jaccard (overlap) entre tokens de todas as respostas
    token_sets: List[set[str]] = []
    for t in texts:
        toks = set([w.lower() for w in t.split() if w])
        token_sets.append(toks)

    n = len(token_sets)
    overlaps: List[float] = []
    for i in range(n):
        for j in range(i + 1, n):
            inter = len(token_sets[i] & token_sets[j])
            union = len(token_sets[i] | token_sets[j])
            overlaps.append(inter / union if union else 0.0)

    similarity = float(sum(overlaps) / max(len(overlaps), 1)) if overlaps else 1.0
    confidence = round(similarity * 0.85 + 0.1, 2)
    # Contexto heurístico baseado no tamanho do texto + similaridade
    context = round(min(1.0, (len(texts[0]) / 200.0) * 0.1 + similarity * 0.75), 2)

    return {"similarity": similarity, "confidence": confidence, "context": context}
