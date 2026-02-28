# ⚪ **Blake AI Orchestrator - Database**

Shared **SQLAlchemy** access module used by the backend.

---

## 🔗 See Also
- [Project overview](../README.md)
- [Backend docs](../backend/README.md)
- [Frontend docs](../frontend/README.md)
- [Monitoring docs](../monitoring/README.md)

---

## 📁 Files
- `database/db.py` → engine, session, `InferenceLog` model, and best-effort initialization.

---

## ⚙️ Configuration
- `DATABASE_URL` → PostgreSQL URL (example: `postgresql://user:pass@db:5432/blake_ai`)

---

## 🧠 Usage in Backend
```python
from database.db import get_session, InferenceLog
```
The backend copies this directory into the Docker image to ensure imports work in production.

---

## 🇧🇷 **PT-BR**

Módulo compartilhado de acesso ao banco (**SQLAlchemy**) usado pelo backend.

---

### 🔗 Veja Também
- [Visão geral do projeto](../README.md)
- [Docs do Backend](../backend/README.md)
- [Docs do Frontend](../frontend/README.md)
- [Docs de Monitoring](../monitoring/README.md)

---

### 📁 Arquivos
- `database/db.py` → engine, sessão, modelo `InferenceLog` e inicialização best-effort.

---

### ⚙️ Configuração
- `DATABASE_URL` → URL do Postgres (exemplo: `postgresql://user:pass@db:5432/blake_ai`)

---

### 🧠 Uso no Backend
```python
from database.db import get_session, InferenceLog
```
O backend copia este diretório na imagem Docker para garantir que os imports funcionem em produção.
