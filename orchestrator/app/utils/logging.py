"""Camada fina sobre Loguru para padronizar logs da aplicação."""
from loguru import logger
import os

os.makedirs("logs", exist_ok=True)
logger.add("logs/orchestrator.log", rotation="10 MB")


def log_info(message: str):
    logger.info(message)
