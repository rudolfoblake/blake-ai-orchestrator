# ⚪ **Blake AI Orchestrator – Monitoring API**

Independent **FastAPI** service to collect backend events and expose **Prometheus metrics**.

---

## 🔗 See Also
- [Project overview](../README.md)
- [Backend docs](../backend/README.md)
- [Frontend docs](../frontend/README.md)
- [Database docs](../database/README.md)

---

## 🧠 Endpoints
- `GET /health` → Service status  
- `POST /collect/inference` → Receives inference events  
- `GET /metrics` → Prometheus metrics  

---

## ⚙️ Local Run
```bash
pip install -r monitoring/requirements.txt
uvicorn api.main:app --host 0.0.0.0 --port 9100
```

---

## 🐳 Docker
- Included in `docker-compose.yml` as **monitoring-api** on port `9100`.

---

## ⚡ Configuration
- `MONITOR_LOG_PATH` *(optional)* → log file path (default: `monitoring/logs/events.log`)

---

## 🇧🇷 **PT-BR**

Serviço **FastAPI** independente para coletar eventos do backend e expor **métricas Prometheus**.

---

### 🔗 Veja Também
- [Visão geral do projeto](../README.md)
- [Docs do Backend](../backend/README.md)
- [Docs do Frontend](../frontend/README.md)
- [Docs de Database](../database/README.md)

---

### 🧠 Endpoints
- `GET /health` → status do serviço  
- `POST /collect/inference` → recebe eventos de inferência  
- `GET /metrics` → métricas Prometheus  

---

### ⚙️ Execução Local
```bash
pip install -r monitoring/requirements.txt
uvicorn api.main:app --host 0.0.0.0 --port 9100
```

---

### 🐳 Docker
- Incluído em `docker-compose.yml` como **monitoring-api** na porta `9100`.

---

### ⚡ Configuração
- `MONITOR_LOG_PATH` *(opcional)* → caminho para o arquivo de log (padrão: `monitoring/logs/events.log`)
