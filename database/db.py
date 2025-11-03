import os
import datetime
from contextlib import contextmanager

from sqlalchemy import create_engine, Column, Integer, Text, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker


DB_URL = os.getenv("DATABASE_URL", "postgresql://user:pass@db:5432/blake_ai")

engine = create_engine(DB_URL, echo=False, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()


class InferenceLog(Base):
    __tablename__ = "inference_logs"
    id = Column(Integer, primary_key=True, index=True)
    prompt = Column(Text, nullable=False)
    outputs = Column(Text, nullable=False)  # JSON string of provider results
    final_response = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)


def init_db():
    try:
        Base.metadata.create_all(bind=engine)
    except Exception:
        # DB may not be up yet; service will attempt on first write
        pass


@contextmanager
def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


# Attempt to initialize tables on import (best-effort)
init_db()