"""
Analisador de respostas dos provedores.

- Carregamento lazy do modelo SentenceTransformer para evitar custo no import.
- Caso a dependência não esteja disponível, usa um fallback por overlap de tokens.
"""
from typing import Dict, Any, List

_ST_MODEL = None
_COSINE = None


def _ensure_model():
    """Garante o carregamento do modelo de embeddings apenas quando necessário."""
    global _ST_MODEL, _COSINE
    if _ST_MODEL is not None:
        return
    try:
        from sklearn.metrics.pairwise import cosine_similarity  # type: ignore
        from sentence_transformers import SentenceTransformer  # type: ignore

        _ST_MODEL = SentenceTransformer("all-MiniLM-L6-v2")
        _COSINE = cosine_similarity
    except Exception:
        _ST_MODEL = None
        _COSINE = None


async def analyze_responses(responses: Dict[str, str]) -> Dict[str, float]:
    """
    Calcula métricas de similaridade/“confiança”/“contexto” entre respostas.
    - Se o SentenceTransformer estiver disponível, usa cosseno de embeddings.
    - Caso contrário, faz fallback para overlap de tokens (Jaccard).
    """
    texts: List[str] = [t or "" for t in responses.values()]
    _ensure_model()
    if _ST_MODEL and _COSINE:
        try:
            embeddings = _ST_MODEL.encode(texts)
            sim_matrix = _COSINE(embeddings)
            n = len(texts)
            if n <= 1:
                similarity = 1.0
            else:
                upper = []
                for i in range(n):
                    for j in range(i + 1, n):
                        upper.append(float(sim_matrix[i][j]))
                similarity = float(sum(upper) / max(len(upper), 1))
            confidence = round(similarity * 0.9 + 0.1, 2)
            context = round(min(1.0, (len(texts[0]) / 200.0) * 0.1 + similarity * 0.8), 2)
            return {"similarity": similarity, "confidence": confidence, "context": context}
        except Exception:
            # Se qualquer etapa do caminho “inteligente” falhar, cai no fallback
            pass

    # Fallback: Jaccard (overlap) entre tokens de todas as respostas
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
    context = round(min(1.0, (len(texts[0]) / 200.0) * 0.1 + similarity * 0.75), 2)
    return {"similarity": similarity, "confidence": confidence, "context": context}
