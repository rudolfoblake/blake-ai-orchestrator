# Database

Shared SQLAlchemy access module used by the backend.

## Files
- `database/db.py`: engine, session, `InferenceLog` model, and best-effort initialization.

## Configuration
- `DATABASE_URL`: Postgres URL (e.g., `postgresql://user:pass@db:5432/blake_ai`)

## Usage in Backend
```
from database.db import get_session, InferenceLog
```

The backend copies this directory into the Docker image to ensure imports work in production.

---

## PT-BR

Módulo compartilhado de acesso ao banco (SQLAlchemy) usado pelo backend.

### Arquivos
- `database/db.py`: engine, sessão, modelo `InferenceLog` e inicialização best-effort.

### Configuração
- `DATABASE_URL`: URL do Postgres (ex.: `postgresql://user:pass@db:5432/blake_ai`)

### Uso no Backend
```
from database.db import get_session, InferenceLog
```

O backend copia este diretório na imagem Docker para garantir que os imports funcionem em produção.