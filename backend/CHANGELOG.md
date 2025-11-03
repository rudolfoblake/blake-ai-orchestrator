# Changelog – Backend

Todas as mudanças relevantes ao serviço de orquestração (FastAPI) ficam listadas aqui.

## 4.0 – Orquestração completa (2025-11-03)
- API alinhada: `POST /infer` retorna `{ final_answer, confidence, sources }`
- Clientes dos provedores: OpenAI, Claude, DeepSeek, Gemini
- `inferencer`: execução paralela (`asyncio.gather`), seleção da melhor resposta e retorno das fontes
- `analyzer`: similaridade com SentenceTransformer e fallback por overlap de tokens
- Configuração via `.env`: personas globais e por provedor, modelos, provedores habilitados, pesos da inferência
- CORS liberado para consumo por qualquer frontend
- Logs e métricas: `/metrics` (Prometheus)

## 3.x – Scaffold inicial
- Estrutura básica do FastAPI, rota `/health`
- Esqueleto de `/infer` com resposta mock
- Configuração inicial de Dockerfile