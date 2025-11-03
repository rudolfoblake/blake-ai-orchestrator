import os
import json
from urllib import request, error


def send_event(payload: dict):
    """Best-effort POST to Monitoring API. Non-blocking callers should run in thread.

    Env:
    - MONITORING_URL: base URL (default http://localhost:9100)
    """
    base = os.getenv("MONITORING_URL", "http://localhost:9100")
    url = base.rstrip("/") + "/collect/inference"
    data = json.dumps(payload).encode("utf-8")
    req = request.Request(url, data=data, headers={"Content-Type": "application/json"})
    try:
        with request.urlopen(req, timeout=5) as resp:
            resp.read()
    except error.URLError:
        pass
    except Exception:
        pass