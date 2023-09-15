from app.database.database import database
from app.models.order import OrderModel
from app.service.product import Product


class Order:
    def __init__(self):
        self.database = database
        self.product_service = Product()

    def create(self, user_id):
        try:
            cart = self.find_cart(user_id)
            if not cart:
                return {"message": "Não possui nada no carrinho para criar o pedido"}

            has_stock = self.verify_stock_products(cart)
            if has_stock is not True:
                return has_stock

            order_data = OrderModel(**cart)
            self.database["order"].insert_one(order_data.dict())

            self.consume_stock(cart.get("itens_cart", []))

            self.remove_cart(user_id)
            return {"message": "Pedido finalizado com sucesso!", "order": order_data}
        except ValueError:
            return False

    def find_cart(self, user_id: str):
        return self.database["shopping_cart"].find_one({"user_id": user_id}, {"_id": 0})

    def remove_cart(self, user_id: str):
        return self.database["shopping_cart"].delete_one({"user_id": user_id})

    def verify_stock_products(self, cart: dict):
        for item in cart.get("itens_cart", []):
            product = self.product_service.find(item.get("product", {}).get("id"))
            if product:
                if item.get("quantity", 0) > product.get("stock", 0):
                    return {
                        "message": f"O produto {product.get('name', '')} só possui {product.get('stock', 0)} unidades no estoque. E você está tentando pedir {item.get('quantity', 0)} unidades."
                    }

        return True

    def consume_stock(self, itens):
        for item in itens:
            product = self.product_service.find(item.get("product", {}).get("id"))
            self.product_service.edit(
                item.get("product", {}).get("id"),
                {"stock": product.get("stock", 0) - item.get("quantity", 0)},
            )

    def all_orders(self, user_id):
        return list(self.database["order"].find({"user_id": user_id}, {"_id": 0}))
