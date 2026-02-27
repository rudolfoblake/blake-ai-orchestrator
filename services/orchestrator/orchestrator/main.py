import os
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator
from starlette.middleware.trustedhost import TrustedHostMiddleware
from starlette.middleware.httpsredirect import HTTPSRedirectMiddleware
from starlette.middleware.gzip import GZipMiddleware

from .router_infer import router as infer_router


def create_app() -> FastAPI:
    """Cria e configura a aplicação FastAPI com middlewares e roteadores."""
    app = FastAPI(title="Blake AI Orchestrator", version="4.0")

    # CORS: restrict to configured origins
    cors_env = os.getenv("CORS_ALLOW_ORIGINS")
    frontend_origin = os.getenv("FRONTEND_ORIGIN", "http://localhost:3000")
    cors_origins = [o.strip() for o in (cors_env.split(",") if cors_env else [frontend_origin]) if o.strip()]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=cors_origins,
        allow_credentials=True,
        allow_methods=["GET", "POST", "OPTIONS"],
        allow_headers=["Content-Type", "Authorization"],
    )
    # Compressão simples de respostas
    app.add_middleware(GZipMiddleware, minimum_size=512)

    # Trusted hosts and optional HTTPS redirect
    allowed_hosts_env = os.getenv("ALLOWED_HOSTS", "localhost,127.0.0.1")
    allowed_hosts = [h.strip() for h in allowed_hosts_env.split(",") if h.strip()]
    app.add_middleware(TrustedHostMiddleware, allowed_hosts=allowed_hosts)
    if os.getenv("FORCE_HTTPS", "false").lower() in ("1", "true", "yes"): 
        app.add_middleware(HTTPSRedirectMiddleware)

    # Basic security headers
    @app.middleware("http")
    async def add_security_headers(request: Request, call_next):
        """Aplica cabeçalhos de segurança básicos em todas as respostas."""
        response = await call_next(request)
        response.headers.setdefault("X-Content-Type-Options", "nosniff")
        response.headers.setdefault("X-Frame-Options", "DENY")
        response.headers.setdefault("Referrer-Policy", "no-referrer")
        response.headers.setdefault("X-XSS-Protection", "1; mode=block")
        return response

    # v4.0: API mounted under /infer
    app.include_router(infer_router, prefix="/infer")

    @app.get("/health")
    def health():
        """Endpoint de verificação de saúde do serviço."""
        return {"status": "ok"}

    Instrumentator().instrument(app).expose(app)
    return app


app = create_app()
