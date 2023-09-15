from datetime import datetime
from typing import List
from uuid import uuid4

from app.models.shopping_cart import ItensCartModel
from pydantic import BaseModel


class OrderModel(BaseModel):
    id: str = None
    user_id: str
    itens_cart: List[ItensCartModel]
    total: float
    created_at: datetime = datetime.now().isoformat()

    def __init__(self, **data):
        if "id" not in data or data["id"] is None:
            data["id"] = str(uuid4())
        super().__init__(**data)
