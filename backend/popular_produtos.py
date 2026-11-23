from database import SessionLocal
from models import Produto

with SessionLocal() as sessao:
    sessao.add(Produto(nome="Mussarela", preco_centavos=3000, categoria="Pizzas"))
    sessao.commit()

print("Produto gravado!")