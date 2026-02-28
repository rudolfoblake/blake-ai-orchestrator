"""
Cache utilitário simples baseado em Redis (opcional).
Exposto via funções cache_get/cache_set para desacoplar chamadas diretas.
"""
import os

try:
    import redis
except Exception:
    redis = None


def get_redis():
    """Retorna um cliente Redis a partir de REDIS_URL, ou None se indisponível."""
    if not redis:
        return None
    url = os.getenv("REDIS_URL", "redis://redis:6379")
    try:
        return redis.Redis.from_url(url)
    except Exception:
        return None


def cache_set(key: str, value: str, ttl: int | None = None):
    """Set com TTL opcional. Retorna True em caso de sucesso."""
    r = get_redis()
    if not r:
        return False
    try:
        if ttl:
            r.setex(key, ttl, value)
        else:
            r.set(key, value)
        return True
    except Exception:
        return False


def cache_get(key: str):
    """Obtém valor bruto (bytes) para a chave; retorna None se indisponível/erro."""
    r = get_redis()
    if not r:
        return None
    try:
        v = r.get(key)
        return v
    except Exception:
        return None
