from fastapi import FastAPI
from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import get_db
from models import Produto

app = FastAPI()

@app.get("/")
def raiz():
    return {"mensagem": "Delivery no ar!"}

@app.get("/cardapio")
def listar_cardapio(db: Session = Depends(get_db)):
    produtos = db.scalars(select(Produto)).all()
    return {"cardapio": [
        {"id": p.id, "nome": p.nome, "preco_centavos": p.preco_centavos, "categoria": p.categoria}
        for p in produtos
    ]}
