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
MIT License — see `LICENSE` at the project root.

## Community
- Contributing — see `CONTRIBUTING.md`
- Code of Conduct — see `CODE_OF_CONDUCT.md`

### Pull Requests & Labels
- Target branch for PRs: `staging` (required).
- Use helpful labels like `bug`, `enhancement`, `help wanted`, `good first issue`.
- Follow the PR template and contribution guide.

---

## PT-BR

Um projeto de portfólio open-source, desacoplado, que demonstra minha stack de engenharia e minha abordagem para construir sistemas com IA. Cada módulo evolui de forma independente e pode rodar sozinho.

### Por que existe
- Demonstra meu portfólio/CV com código real: padrões de orquestração, APIs limpas, Python tipado, um cliente React simples e observabilidade.
- Prioriza separação de responsabilidades e arquitetura modular, permitindo trocar componentes sem quebrar o sistema inteiro.
- Serve como sandbox de aprendizado e experimentação mantendo práticas de produção: serviços Dockerizados, health checks, métricas e docs de API gerados automaticamente.

### Módulos
- `backend/`: API FastAPI que orquestra provedores de IA; expõe `POST /infer`.
- `frontend/`: App React leve que chama o backend e renderiza resultados.
- `database/`: Módulo compartilhado de acesso ao banco (SQLAlchemy) usado pelo backend.
- `monitoring/`: Serviço FastAPI independente para coletar eventos e métricas Prometheus.

### Quickstart
- Docker:
  - `docker compose up --build`
  - Serviços:
    - Backend: `http://localhost:8000` (saúde: `/health`, métricas: `/metrics`)
    - Frontend: `http://localhost:3000`
    - Monitoring API: `http://localhost:9100` (saúde: `/health`, métricas: `/metrics`)
    - Prometheus: `http://localhost:9090`
    - Grafana: `http://localhost:4000`
- Desenvolvimento local:
  - Backend: `pip install -r backend/requirements.txt && uvicorn backend.orchestrator.main:app --reload`
  - Frontend: `cd frontend && npm install && npm start`

### Docs de API
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`
- OpenAPI JSON: `http://localhost:8000/openapi.json`

### Documentação do projeto
- Backend: `backend/README.md`
- Frontend: `frontend/README.md`
- Monitoring: `monitoring/README.md`
- Database: `database/README.md`
- Changelogs por projeto: `backend/CHANGELOG.md`, `frontend/CHANGELOG.md`

### Licença
Licença MIT — veja `LICENSE` na raiz do projeto.

### Comunidade
- Contribuição — veja `CONTRIBUTING.md`
- Código de Conduta — veja `CODE_OF_CONDUCT.md`

#### Pull Requests & Labels (PT-BR)
- Branch alvo dos PRs: `staging` (obrigatório).
- Utilize labels úteis como `bug`, `enhancement`, `help wanted`, `good first issue`.
- Siga o template de PR e o guia de contribuição.