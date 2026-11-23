from database import SessionLocal
from models import Produto

with SessionLocal() as sessao:
    sessao.add(Produto(nome="Mussarela", preco_centavos=3000, categoria="Pizzas"))
    sessao.add(Produto(nome="Classico", preco_centavos=2000, categoria="Hambúrgueres"))
    sessao.add(Produto(nome="California Roll", preco_centavos=5000, categoria="Sushi"))  
    sessao.add(Produto(nome="Vitamina", preco_centavos=2000, categoria="Açaí"))  
    sessao.commit()

print("Produto gravado!")
