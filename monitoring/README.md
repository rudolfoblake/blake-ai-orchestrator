# Monitoring API

Independent FastAPI service to collect backend events and expose Prometheus metrics.

## Endpoints
- `GET /health`: service status
- `POST /collect/inference`: receives inference events
- `GET /metrics`: Prometheus metrics

## Local Run
```
pip install -r monitoring/requirements.txt
uvicorn api.main:app --host 0.0.0.0 --port 9100
```

## Docker
- Included in `docker-compose.yml` as `monitoring-api` on port `9100`.

## Configuration
- `MONITOR_LOG_PATH` (optional): log file path (`monitoring/logs/events.log` by default)

---

## PT-BR

Serviço FastAPI independente para coletar eventos do backend e expor métricas Prometheus.

### Endpoints
- `GET /health`: status do serviço
- `POST /collect/inference`: recebe eventos de inferência
- `GET /metrics`: métricas Prometheus

### Execução local
```
pip install -r monitoring/requirements.txt
uvicorn api.main:app --host 0.0.0.0 --port 9100
```

### Docker
- Incluído em `docker-compose.yml` como `monitoring-api` na porta `9100`.

### Configuração
- `MONITOR_LOG_PATH` (opcional): caminho para arquivo de log (`monitoring/logs/events.log` por padrão)