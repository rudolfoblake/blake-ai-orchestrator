# Blake AI Orchestrator

A decoupled portfolio project showcasing my stack. Each part evolves independently.

## Structure
- `backend/`: FastAPI API orchestrating AI providers; exposes `POST /infer`.
- `frontend/`: Lightweight React app consuming the backend.
- `database/`: Shared SQLAlchemy access module used by the backend.
- `monitoring/`: Independent FastAPI service for event collection and Prometheus metrics.

## Run
- Docker:
  - `docker compose up --build`
  - Services:
    - Backend: `http://localhost:8000` (health: `/health`, metrics: `/metrics`)
    - Frontend: `http://localhost:3000`
    - Monitoring API: `http://localhost:9100` (health: `/health`, metrics: `/metrics`)
    - Prometheus: `http://localhost:9090`
    - Grafana: `http://localhost:4000`
- Local dev:
  - Backend: `pip install -r backend/requirements.txt && uvicorn backend.orchestrator.main:app --reload`
  - Frontend: `cd frontend && npm install && npm start`

## Documentation
- Backend: `backend/README.md`
- Frontend: `frontend/README.md`
- Per-project changelogs: `backend/CHANGELOG.md`, `frontend/CHANGELOG.md`

License: see `LICENSE` at the root.

---

## PT-BR

Projeto desacoplado de portfólio demonstrando minha stack. Cada parte evolui de forma independente.

### Estrutura
- `backend/`: API FastAPI que orquestra provedores de IA; expõe `POST /infer`.
- `frontend/`: App React leve que consome o backend.
- `database/`: Módulo compartilhado de acesso ao banco (SQLAlchemy) usado pelo backend.
- `monitoring/`: Serviço FastAPI independente para coletar eventos e métricas Prometheus.

### Como rodar
- Docker:
  - `docker compose up --build`
  - Serviços:
    - Backend: `http://localhost:8000` (saúde: `/health`, métricas: `/metrics`)
    - Frontend: `http://localhost:3000`
    - Monitoring API: `http://localhost:9100` (saúde: `/health`, métricas: `/metrics`)
    - Prometheus: `http://localhost:9090`
    - Grafana: `http://localhost:4000`
- Dev local:
  - Backend: `pip install -r backend/requirements.txt && uvicorn backend.orchestrator.main:app --reload`
  - Frontend: `cd frontend && npm install && npm start`

### Documentação
- Backend: `backend/README.md`
- Frontend: `frontend/README.md`
- Changelogs por projeto: `backend/CHANGELOG.md`, `frontend/CHANGELOG.md`

Licença: veja `LICENSE` na raiz.