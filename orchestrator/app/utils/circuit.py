"""
Circuit breaker simples por provedor (in-memory).
Evita chamadas repetidas a provedores instáveis abrindo o circuito por um cooldown.
"""
from __future__ import annotations

import os
import time
from dataclasses import dataclass
from typing import Dict


@dataclass
class Breaker:
    failures: int = 0
    open_until: float = 0.0
    threshold: int = 5
    cooldown: float = 30.0

    def allow(self) -> bool:
        return time.time() >= self.open_until

    def fail(self):
        self.failures += 1
        if self.failures >= self.threshold:
            self.open_until = time.time() + self.cooldown
            self.failures = 0

    def success(self):
        self.failures = 0
        self.open_until = 0.0


_breakers: Dict[str, Breaker] = {}


def _get_threshold(name: str) -> int:
    env_key = f"CB_THRESHOLD_{name.upper()}"
    try:
        return int(os.getenv(env_key) or os.getenv("CB_THRESHOLD_DEFAULT", "5"))
    except Exception:
        return 5


def _get_cooldown(name: str) -> float:
    env_key = f"CB_COOLDOWN_{name.upper()}"
    try:
        return float(os.getenv(env_key) or os.getenv("CB_COOLDOWN_DEFAULT", "30"))
    except Exception:
        return 30.0


def get_breaker(name: str) -> Breaker:
    b = _breakers.get(name)
    if b is None:
        b = Breaker(threshold=_get_threshold(name), cooldown=_get_cooldown(name))
        _breakers[name] = b
    return b
