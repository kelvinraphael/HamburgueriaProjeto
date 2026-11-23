import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

raiz = Path(__file__).resolve().parent.parent
load_dotenv(raiz / ".env")

usuario = os.getenv("DB_USER")
senha = os.getenv("DB_PASSWORD")
banco = os.getenv("DB_NAME")

URL_BANCO = f"postgresql+psycopg://{usuario}:{senha}@localhost:5433/{banco}"

engine = create_engine(URL_BANCO)
SessionLocal = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass

def get_db():
    with SessionLocal() as sessao:
        yield sessao