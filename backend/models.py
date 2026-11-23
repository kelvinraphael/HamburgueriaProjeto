from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class Produto(Base):
    __tablename__ = "produtos"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(100))
    preco_centavos: Mapped[int]
    categoria: Mapped[str] = mapped_column(String(50))