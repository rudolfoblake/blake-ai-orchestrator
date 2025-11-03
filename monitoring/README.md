# Monitoring API

Serviço FastAPI independente para coleta de eventos do backend e exposição de métricas Prometheus.

## Endpoints
- `GET /health`: status do serviço
- `POST /collect/inference`: recebe eventos de inferência
- `GET /metrics`: métricas Prometheus

## Execução local
```
pip install -r monitoring/requirements.txt
uvicorn api.main:app --host 0.0.0.0 --port 9100
```

## Docker
- Incluído no `docker-compose.yml` como `monitoring-api` na porta `9100`.

## Configuração
- `MONITOR_LOG_PATH` (opcional): caminho para arquivo de log (`monitoring/logs/events.log` por padrão)