# Robust analyzer with optional sentence-transformers; fallback to token overlap
import math

try:
    from sklearn.metrics.pairwise import cosine_similarity  # type: ignore
    from sentence_transformers import SentenceTransformer  # type: ignore
    _st_model = SentenceTransformer("all-MiniLM-L6-v2")
except Exception:
    _st_model = None
    cosine_similarity = None


async def analyze_responses(responses: dict):
    texts = [t or "" for t in responses.values()]
    if _st_model and cosine_similarity:
        try:
            embeddings = _st_model.encode(texts)
            sim_matrix = cosine_similarity(embeddings)
            # mean of upper triangle (pairwise similarities)
            n = len(texts)
            if n <= 1:
                similarity = 1.0
            else:
                upper = []
                for i in range(n):
                    for j in range(i + 1, n):
                        upper.append(sim_matrix[i][j])
                similarity = float(sum(upper) / max(len(upper), 1))
            confidence = round(similarity * 0.9 + 0.1, 2)
            context = round(min(1.0, (len(texts[0]) / 200.0) * 0.1 + similarity * 0.8), 2)
            return {"similarity": similarity, "confidence": confidence, "context": context}
        except Exception:
            pass
    # Fallback: Jaccard token overlap across all responses
    token_sets = []
    for t in texts:
        toks = set([w.lower() for w in t.split() if w])
        token_sets.append(toks)
    n = len(token_sets)
    overlaps = []
    for i in range(n):
        for j in range(i + 1, n):
            inter = len(token_sets[i] & token_sets[j])
            union = len(token_sets[i] | token_sets[j])
            overlaps.append(inter / union if union else 0.0)
    similarity = float(sum(overlaps) / max(len(overlaps), 1)) if overlaps else 1.0
    confidence = round(similarity * 0.85 + 0.1, 2)
    context = round(min(1.0, (len(texts[0]) / 200.0) * 0.1 + similarity * 0.75), 2)
    return {"similarity": similarity, "confidence": confidence, "context": context}