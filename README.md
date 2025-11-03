# Blake AI Orchestrator

Projeto open source que serve como meu portfólio e currículo para demonstrar as stacks que utilizo. O repositório é organizado de forma desacoplada para que cada parte possa evoluir independentemente.

## Estrutura
- `backend/`: API FastAPI que orquestra provedores de IA e expõe `POST /infer`.
- `frontend/`: App React simples que consome o backend.
- `database/`: Módulo comum de acesso ao banco (SQLAlchemy), compartilhado pelo backend.
- `monitoring/`: Serviço FastAPI independente para coleta de eventos e métricas Prometheus.

## Como rodar
- Docker:
  - `docker compose up --build`
  - Serviços:
    - Backend: `http://localhost:8000` (health: `/health`, métricas: `/metrics`)
    - Frontend: `http://localhost:3000`
    - Monitoring API: `http://localhost:9100` (health: `/health`, métricas: `/metrics`)
    - Prometheus: `http://localhost:9090`
    - Grafana: `http://localhost:4000`
- Dev local:
  - Backend: `pip install -r backend/requirements.txt && uvicorn backend.orchestrator.main:app --reload`
  - Frontend: `cd frontend && npm install && npm start`

## Documentação
- Backend: `backend/README.md`
- Frontend: `frontend/README.md`
- Changelogs por projeto: `backend/CHANGELOG.md` e `frontend/CHANGELOG.md`

Licença: veja `LICENSE` na raiz.