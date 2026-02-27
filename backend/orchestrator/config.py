import os


class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://user:pass@db:5432/blake_ai")
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://redis:6379")
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    CACHE_TTL: int = int(os.getenv("CACHE_TTL", "300"))
    MAX_TOKENS: int = int(os.getenv("MAX_TOKENS", "2048"))
    TEMPERATURE: float = float(os.getenv("TEMPERATURE", "0.7"))
    INFER_WEIGHT_SIMILARITY: float = float(os.getenv("INFER_WEIGHT_SIMILARITY", "0.4"))
    INFER_WEIGHT_CONFIDENCE: float = float(os.getenv("INFER_WEIGHT_CONFIDENCE", "0.3"))
    INFER_WEIGHT_CONTEXT: float = float(os.getenv("INFER_WEIGHT_CONTEXT", "0.3"))


settings = Settings()