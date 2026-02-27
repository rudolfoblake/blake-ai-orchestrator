import os
import time
from typing import Dict, Any, Optional

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from prometheus_client import Counter, Histogram, Gauge, generate_latest, CONTENT_TYPE_LATEST
from starlette.responses import Response


class InferenceEvent(BaseModel):
    prompt: str
    final_answer: Optional[str] = None
    confidence: Optional[float] = None
    sources: Optional[Dict[str, str]] = None
    providers: Optional[list[str]] = None
    duration_ms: Optional[float] = None
    error: Optional[str] = None


app = FastAPI(title="Monitoring API", version="1.0.0")

# Restrict CORS to configured origins
monitor_origins_env = os.environ.get("MONITOR_ALLOWED_ORIGINS",
                                    "http://localhost:8000,http://localhost:3000")
monitor_origins = [o.strip() for o in monitor_origins_env.split(",") if o.strip()]
app.add_middleware(
    CORSMiddleware,
    allow_origins=monitor_origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization"],
)


# Prometheus metrics
INFER_EVENTS = Counter(
    "monitor_infer_events_total",
    "Total inference events received",
    ["status"],
)

INFER_DURATION = Histogram(
    "monitor_infer_duration_ms",
    "Reported inference durations in ms",
)

CONFIDENCE_GAUGE = Gauge(
    "monitor_infer_last_confidence",
    "Confidence of last received inference",
)


LOG_PATH = os.environ.get("MONITOR_LOG_PATH", os.path.join("monitoring", "logs", "events.log"))
os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/collect/inference")
async def collect_inference(event: InferenceEvent, request: Request):
    received_at = time.time()
    status = "ok" if event.error is None else "error"
    INFER_EVENTS.labels(status=status).inc()

    if event.duration_ms is not None:
        try:
            INFER_DURATION.observe(float(event.duration_ms))
        except Exception:
            pass

    if event.confidence is not None:
        try:
            CONFIDENCE_GAUGE.set(float(event.confidence))
        except Exception:
            pass

    # Append JSON line to log file (with optional redaction)
    try:
        import json
        payload: Dict[str, Any] = event.dict()
        if os.environ.get("MONITOR_REDACT", "true").lower() in ("1", "true", "yes"):
            payload["prompt"] = "[redacted]"
            payload["final_answer"] = "[redacted]"
            payload["sources"] = {}
        payload["received_at"] = received_at
        payload["client_ip"] = request.client.host if request.client else None
        with open(LOG_PATH, "a", encoding="utf-8") as f:
            f.write(json.dumps(payload, ensure_ascii=False) + "\n")
    except Exception:
        # best-effort logging; keep API responsive
        pass

    return {"status": status}


@app.get("/metrics")
def metrics():
    data = generate_latest()
    return Response(content=data, media_type=CONTENT_TYPE_LATEST)