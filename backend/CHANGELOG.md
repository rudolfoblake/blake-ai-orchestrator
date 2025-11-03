# Changelog – Backend

All relevant changes to the orchestration service (FastAPI) are listed here.

## 4.0 – Full orchestration (2025-11-03)
- API aligned: `POST /infer` returns `{ final_answer, confidence, sources }`
- Provider clients: OpenAI, Claude, DeepSeek, Gemini
- `inferencer`: parallel execution (`asyncio.gather`), best-answer selection, returns sources
- `analyzer`: similarity via SentenceTransformer with token-overlap fallback
- `.env` configuration: global and per-provider personas, models, enabled providers, inference weights
- CORS enabled for consumption by any frontend
- Logs and metrics: `/metrics` (Prometheus)

## 3.x – Initial scaffold
- Basic FastAPI structure, `/health` route
- `/infer` skeleton with mock response
- Initial Dockerfile configuration