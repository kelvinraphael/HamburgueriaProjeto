from fastapi import FastAPI
from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from schemas import ProdutoOut
from database import get_db
from models import Produto

app = FastAPI()

@app.get("/")
def raiz():
    return {"mensagem": "Delivery no ar!"}

@app.get("/cardapio", response_model=list[ProdutoOut]) 
def listar_cardapio(db: Session = Depends(get_db)):
    
    produtos = db.scalars(select(Produto)).all()
    return produtos
