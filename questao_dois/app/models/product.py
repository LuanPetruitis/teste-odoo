from datetime import datetime
from uuid import uuid4

from pydantic import BaseModel


# Não adicionei o id pois o mongo cria um _id automático
class ProductModel(BaseModel):
    id: str = None
    name: str
    price: float
    stock: int
    created_at: datetime = datetime.now().isoformat()

    def __init__(self, **data):
        if "id" not in data or data["id"] is None:
            data["id"] = str(uuid4())
        super().__init__(**data)


class ProductEditModel(BaseModel):
    name: str
    price: float
    stock: int
