# ⚪ **Blake AI Orchestrator – Backend**

FastAPI backend orchestrating multiple AIs (**OpenAI**, **Claude**, **DeepSeek**, **Gemini**), running parallel calls and aggregating into a final inference.

---

## 🔗 See Also
- [Project overview](../README.md)
- [Frontend docs](../frontend/README.md)
- [Monitoring docs](../monitoring/README.md)
- [Database docs](../database/README.md)

---

## ⚙️ Requirements
- Python 3.11
- Optional: Redis and PostgreSQL for cache and logs

---

## 🧠 Setup
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
pip install -r backend/requirements.txt
```

---

## 🚀 Run
```bash
uvicorn backend.orchestrator.main:app --reload
```
- API → [http://localhost:8000](http://localhost:8000)  
- Health → `GET /health`  
- Inference → `POST /infer` → `{ "prompt": "..." }`  
- Metrics → `GET /metrics`  
- Docs → [Swagger](http://localhost:8000/docs) | [ReDoc](http://localhost:8000/redoc)

---

## 🌍 Environment Variables
See `.env.example` at the project root. Highlights:

- Keys → `OPENAI_API_KEY`, `CLAUDE_API_KEY`, `DEEPSEEK_API_KEY`, `GEMINI_API_KEY`  
- Enabled providers → `ENABLED_PROVIDERS=openai,claude,deepseek,gemini`  
- Personas → `PERSONA_DEFAULT`, `PERSONA_OPENAI`, `PERSONA_CLAUDE`, etc.  
- Models → `OPENAI_MODEL`, `CLAUDE_MODEL`, `DEEPSEEK_MODEL`, `GEMINI_MODEL`  
- Params → `TEMPERATURE`, `MAX_TOKENS`, weights `INFER_WEIGHT_*`  
- Infra → `DATABASE_URL`, `REDIS_URL`  

---

## 🧩 Flow
1. `POST /infer` receives `{ prompt }`
2. `services/inferencer.py` fires async calls to enabled providers
3. `services/analyzer.py` computes similarity/confidence/context (SentenceTransformer/fallback)
4. Returns `{ final_answer, confidence, sources }`

---

## 🪶 Decoupling
- Fully independent backend; serves any frontend via REST  
- CORS open (`*`) by default → adjust as needed  
- Redis/Postgres optional → API runs standalone  

---

## 🧱 Structure
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

---

## 🧪 Quick Test
```bash
curl -X POST http://localhost:8000/infer   -H "Content-Type: application/json"   -d '{"prompt":"Explain AI in the creative economy"}'
```

---

## 🇧🇷 **PT-BR**

Backend **FastAPI** que orquestra múltiplas IAs (**OpenAI**, **Claude**, **DeepSeek**, **Gemini**), realiza chamadas paralelas e combina respostas em uma inferência final.

---

### 🔗 Veja Também
- [Visão geral do projeto](../README.md)
- [Docs do Frontend](../frontend/README.md)
- [Docs de Monitoring](../monitoring/README.md)
- [Docs de Database](../database/README.md)

---

### ⚙️ Requisitos
- Python 3.11  
- (Opcional) Redis e PostgreSQL para cache e logs

---

### 🧠 Instalação
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
pip install -r backend/requirements.txt
```

---

### 🚀 Execução
```bash
uvicorn backend.orchestrator.main:app --reload
```
- API → [http://localhost:8000](http://localhost:8000)  
- Saúde → `GET /health`  
- Inferência → `POST /infer` → `{ "prompt": "..." }`  
- Métricas Prometheus → `GET /metrics`  
- Docs → [Swagger](http://localhost:8000/docs) | [ReDoc](http://localhost:8000/redoc)

---

### 🌍 Variáveis de Ambiente
Veja `.env.example` na raiz do projeto. Principais:

- Chaves → `OPENAI_API_KEY`, `CLAUDE_API_KEY`, `DEEPSEEK_API_KEY`, `GEMINI_API_KEY`  
- Provedores habilitados → `ENABLED_PROVIDERS=openai,claude,deepseek,gemini`  
- Personas → `PERSONA_DEFAULT`, `PERSONA_OPENAI`, `PERSONA_CLAUDE`, etc.  
- Modelos → `OPENAI_MODEL`, `CLAUDE_MODEL`, `DEEPSEEK_MODEL`, `GEMINI_MODEL`  
- Parâmetros → `TEMPERATURE`, `MAX_TOKENS`, pesos `INFER_WEIGHT_*`  
- Infra → `DATABASE_URL`, `REDIS_URL`  

---

### 🔁 Fluxo
1. `POST /infer` recebe `{ prompt }`
2. `services/inferencer.py` dispara chamadas assíncronas aos provedores habilitados
3. `services/analyzer.py` calcula similaridade/confiança/contexto (SentenceTransformer/fallback)
4. Retorna `{ final_answer, confidence, sources }`

---

### 🪶 Desacoplamento
- Backend totalmente independente; expõe REST para qualquer frontend  
- CORS liberado (`*`) por padrão; ajuste conforme necessidade  
- Redis e Postgres opcionais; a API funciona sem eles  

---

### 🧱 Estrutura
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

---

### 🧪 Teste Rápido
```bash
curl -X POST http://localhost:8000/infer   -H "Content-Type: application/json"   -d '{"prompt":"Explique IA na economia criativa"}'
```
