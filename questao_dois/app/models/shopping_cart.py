from app.models.product import ProductModel
from pydantic import BaseModel


class ItensCartModel(BaseModel):
    product: ProductModel
    quantity: int


class ItemCart(BaseModel):
    product_id: str
    quantity: int
