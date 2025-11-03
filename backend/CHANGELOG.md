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

---

## PT-BR

Todas as mudanças relevantes ao serviço de orquestração (FastAPI) estão listadas aqui.

### 4.0 – Orquestração completa (2025-11-03)
- API alinhada: `POST /infer` retorna `{ final_answer, confidence, sources }`
- Clientes dos provedores: OpenAI, Claude, DeepSeek, Gemini
- `inferencer`: execução paralela (`asyncio.gather`), seleção da melhor resposta e retorno das fontes
- `analyzer`: similaridade com SentenceTransformer e fallback por overlap de tokens
- Configuração via `.env`: personas globais e por provedor, modelos, provedores habilitados, pesos da inferência
- CORS liberado para consumo por qualquer frontend
- Logs e métricas: `/metrics` (Prometheus)

### 3.x – Scaffold inicial
- Estrutura básica do FastAPI, rota `/health`
- Esqueleto de `/infer` com resposta mock
- Configuração inicial de Dockerfile