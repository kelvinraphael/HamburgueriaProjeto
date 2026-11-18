from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def raiz():
    return {"mensagem": "Delivery no ar!"}

@app.get("/cardapio")
def cardapio():
    return {"cardapio": [
        {"id": 1, "nome": "Mussarela", "preco": 30.0, "categoria": "Pizzas"},
        {"id": 2, "nome": "Classico", "preco": 20.0, "categoria": "Hambúrgueres"},
        {"id": 3, "nome": "California Roll", "preco": 50.0, "categoria": "Sushi"},
        {"id": 4, "nome": "Vitamina", "preco": 20.0, "categoria": "Açaí"},   
    ]}