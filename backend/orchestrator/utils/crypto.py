import os
from typing import Optional

try:
    from cryptography.fernet import Fernet
except Exception:
    Fernet = None  # cryptography may not be installed yet


def _get_key() -> Optional[bytes]:
    key = os.getenv("LOG_ENCRYPTION_KEY", "").strip()
    if not key:
        return None
    return key.encode("utf-8")


def get_fernet() -> Optional["Fernet"]:
    if Fernet is None:
        return None
    key = _get_key()
    if not key:
        return None
    try:
        return Fernet(key)
    except Exception:
        return None


def encrypt_if_configured(value: str) -> str:
    """Encrypts value using Fernet when LOG_ENCRYPTION_KEY is set; otherwise returns original."""
    f = get_fernet()
    if not f:
        return value
    if value is None:
        value = ""
    try:
        return f.encrypt(value.encode("utf-8")).decode("utf-8")
    except Exception:
        return value