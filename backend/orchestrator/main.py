import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator

from .router_infer import router as infer_router


def create_app() -> FastAPI:
    app = FastAPI(title="Blake AI Orchestrator", version="4.0")

    frontend_origin = os.getenv("FRONTEND_ORIGIN", "http://localhost:3000")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[frontend_origin, "*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # v4.0: API mounted under /infer
    app.include_router(infer_router, prefix="/infer")

    @app.get("/health")
    def health():
        return {"status": "ok"}

    Instrumentator().instrument(app).expose(app)
    return app


app = create_app()