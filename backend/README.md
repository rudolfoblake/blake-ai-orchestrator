# Blake AI Orchestrator – Backend

Backend FastAPI que orquestra múltiplas IAs (OpenAI, Claude, DeepSeek, Gemini), realiza chamadas paralelas e combina respostas em uma inferência final.

## Requisitos
- Python 3.11
- (Opcional) Redis e PostgreSQL para cache e logs

## Instalação
```
python -m venv .venv
.venv\\Scripts\\activate  # Windows
pip install -r backend/requirements.txt
```

## Execução
```
uvicorn backend.orchestrator.main:app --reload
```
- API: `http://localhost:8000`
- Health: `GET /health`
- Inferência: `POST /infer` (body: `{ "prompt": "..." }`)
- Métricas Prometheus: `GET /metrics`
- Docs: `http://localhost:8000/docs` e `http://localhost:8000/redoc`

## Variáveis de Ambiente
Veja `.env.example` na raiz do projeto. Principais:
- Chaves: `OPENAI_API_KEY`, `CLAUDE_API_KEY`, `DEEPSEEK_API_KEY`, `GEMINI_API_KEY`
- Provedores habilitados: `ENABLED_PROVIDERS=openai,claude,deepseek,gemini`
- Personas: `PERSONA_DEFAULT` e por provedor (`PERSONA_OPENAI`, `PERSONA_CLAUDE`, etc.)
- Modelos: `OPENAI_MODEL`, `CLAUDE_MODEL`, `DEEPSEEK_MODEL`, `GEMINI_MODEL`
- Parâmetros: `TEMPERATURE`, `MAX_TOKENS`, pesos `INFER_WEIGHT_*`
- Infra: `DATABASE_URL`, `REDIS_URL`

## Fluxo
1. `POST /infer` recebe `{ prompt }`
2. `services/inferencer.py` dispara chamadas assíncronas aos provedores habilitados
3. `services/analyzer.py` calcula similaridade/confiança/contexto (SentenceTransformer/fallback)
4. Resposta: `{ final_answer, confidence, sources }`

## Desacoplamento
- O backend é totalmente independente e expõe REST para qualquer frontend
- CORS está liberado (`*`) por padrão; ajuste conforme necessidade
- Redis e Postgres são opcionais (best-effort); a API funciona sem eles

## Estrutura
```
orchestrator/
  main.py
  router_infer.py
  services/
    openai_client.py
    claude_client.py
    deepseek_client.py
    gemini_client.py
    analyzer.py
    inferencer.py
  utils/
    logging.py
    cache.py
    database.py
  __init__.py
```

## Teste rápido
```
curl -X POST http://localhost:8000/infer \
  -H "Content-Type: application/json" \
  -d '{"prompt":"Explique IA na economia criativa"}'
```