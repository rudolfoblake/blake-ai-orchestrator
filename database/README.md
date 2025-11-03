# Database

Módulo comum de acesso ao banco (SQLAlchemy) compartilhado pelo backend.

## Arquivos
- `database/db.py`: engine, sessão, modelo `InferenceLog` e inicialização best-effort.

## Configuração
- `DATABASE_URL`: URL do Postgres (ex.: `postgresql://user:pass@db:5432/blake_ai`)

## Uso no Backend
```
from database.db import get_session, InferenceLog
```

O backend copia este diretório na imagem Docker para garantir que os imports funcionem em produção.