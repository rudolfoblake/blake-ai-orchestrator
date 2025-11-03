# Blake AI Orchestrator

An open-source, decoupled portfolio project that showcases my engineering stack and approach to building AI-enabled systems. Each module evolves independently and can run on its own.

## Why This Exists
- Demonstrates my portfolio/CV through real code: orchestration patterns, clean APIs, typed Python, a small React client, and observability.
- Prioritizes separation of concerns and modular architecture, so components can be swapped or improved without breaking the whole system.
- Serves as a learning and experimentation sandbox while remaining production-friendly: Dockerized services, health checks, metrics, and auto-generated API docs.

## Modules
- `backend/`: FastAPI API orchestrating AI providers; exposes `POST /infer`.
- `frontend/`: Lightweight React app that calls the backend and renders results.
- `database/`: Shared SQLAlchemy access module used by the backend.
- `monitoring/`: Independent FastAPI service for event collection and Prometheus metrics.

## Quickstart
- Docker:
  - `docker compose up --build`
  - Services:
    - Backend: `http://localhost:8000` (health: `/health`, metrics: `/metrics`)
    - Frontend: `http://localhost:3000`
    - Monitoring API: `http://localhost:9100` (health: `/health`, metrics: `/metrics`)
    - Prometheus: `http://localhost:9090`
    - Grafana: `http://localhost:4000`
- Local development:
  - Backend: `pip install -r backend/requirements.txt && uvicorn backend.orchestrator.main:app --reload`
  - Frontend: `cd frontend && npm install && npm start`

## API Docs
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`
- OpenAPI JSON: `http://localhost:8000/openapi.json`

## Project Documentation
- Backend: `backend/README.md`
- Frontend: `frontend/README.md`
- Monitoring: `monitoring/README.md`
- Database: `database/README.md`
- Per-project changelogs: `backend/CHANGELOG.md`, `frontend/CHANGELOG.md`

## License
Open-source license — see `LICENSE` at the project root.