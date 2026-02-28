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
orchestrator/ → FastAPI orchestrator (POST /infer) + DB module
frontend/     → Lightweight React client
```

---

## 🚀 Quickstart

### Docker
```bash
cp .env.example .env
docker compose up --build
```

**Services**
- Orchestrator → [http://localhost:8000](http://localhost:8000)  
- Frontend → [http://localhost:3000](http://localhost:3000)

### Local Dev
```bash
cd orchestrator && pip install -r requirements.txt
uvicorn app.main:app --reload

cd ../frontend && npm install && npm start
```

---

## 📘 API Docs
- Swagger → [http://localhost:8000/docs](http://localhost:8000/docs)  
- ReDoc → [http://localhost:8000/redoc](http://localhost:8000/redoc)  
- OpenAPI → [http://localhost:8000/openapi.json](http://localhost:8000/openapi.json)

---

## 🧩 Documentation
- [orchestrator/README.md](orchestrator/README.md)  
- [frontend/README.md](frontend/README.md)

---

## 🪪 License
**MIT License** — see [LICENSE](LICENSE)

---

## 🤝 Contribute
- Branch target: `staging`  
- Use labels: `bug`, `enhancement`, `help wanted`, `good first issue`  
- Follow PR template & code of conduct  
