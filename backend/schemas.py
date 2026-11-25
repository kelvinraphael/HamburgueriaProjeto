from pydantic import BaseModel, ConfigDict


class ProdutoOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    nome: str
    preco_centavos: int
    categoria: str