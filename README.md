# ⚪ **Blake AI Orchestrator**

Open-source, modular portfolio showcasing my engineering stack and approach to AI-enabled systems.  
Each module is **fully decoupled**, evolving on its own.

---

## ✳️ Why It Exists
- A living portfolio: **real code, real orchestration**, not slides.  
- Modular by design: swap or improve components without breaking the rest.  
- Clean, typed **Python + FastAPI**, **React**, **observability**, **Docker**, and **metrics**.  
- Built for clarity, scalability, and calm engineering.

---

## ⚙️ Modules
```
backend/     → FastAPI orchestrator (POST /infer)
frontend/    → Lightweight React client
database/    → Shared SQLAlchemy layer
monitoring/  → Metrics & Prometheus collector
```

---

## 🚀 Quickstart

### Docker
```bash
cp .env.example .env
docker compose up --build
```

**Services**
- Backend → [http://localhost:8000](http://localhost:8000)  
- Frontend → [http://localhost:3000](http://localhost:3000)  
- Monitoring → [http://localhost:9100](http://localhost:9100)  
- Prometheus → [http://localhost:9090](http://localhost:9090)  
- Grafana → [http://localhost:4000](http://localhost:4000)

### Local Dev
```bash
pip install -r backend/requirements.txt
uvicorn backend.orchestrator.main:app --reload

cd frontend && npm install && npm start
```

---

## 📘 API Docs
- Swagger → [http://localhost:8000/docs](http://localhost:8000/docs)  
- ReDoc → [http://localhost:8000/redoc](http://localhost:8000/redoc)  
- OpenAPI → [http://localhost:8000/openapi.json](http://localhost:8000/openapi.json)

---

## 🧩 Documentation
- [backend/README.md](backend/README.md)  
- [frontend/README.md](frontend/README.md)  
- [monitoring/README.md](monitoring/README.md)  
- [database/README.md](database/README.md)  
- [backend/CHANGELOG.md](backend/CHANGELOG.md), [frontend/CHANGELOG.md](frontend/CHANGELOG.md)

---

## 🪪 License
**MIT License** — see [LICENSE](LICENSE)

---

## 🤝 Contribute
- Branch target: `staging`  
- Use labels: `bug`, `enhancement`, `help wanted`, `good first issue`  
- Follow PR template & code of conduct  
