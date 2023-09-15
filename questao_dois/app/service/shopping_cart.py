from app.database.database import DBConnection


class ShoppingCart:
    def __init__(self):
        self.database = DBConnection().database

    def add_product(self, user_id, data):
        try:
            cart = self.find_cart(user_id)
            if not cart:
                self.database["shopping_cart"].insert_one(
                    {
                        "user_id": user_id,
                        "itens_cart": [data],
                        "total": self.calculate_total_product(data),
                    }
                )
                return True

            return self.update_cart(user_id, cart, data)
        except ValueError:
            return False

    def update_cart(self, user_id, cart, data):
        itens_cart = []
        product_already_itens = False
        total = cart.get("total", 0) + (self.calculate_total_product(data))
        for item in cart.get("itens_cart", []):
            if item.get("product", {}).get("id") == data.get("product", {}).get(
                "id", 0
            ):
                product_already_itens = True
                item["quantity"] = item.get("quantity", 1) + data.get("quantity", 1)
            itens_cart.append(item)

        if not product_already_itens:
            itens_cart.append(data)

        self.database["shopping_cart"].update_one(
            {"user_id": user_id},
            {
                "$set": {
                    "itens_cart": itens_cart,
                    "total": total,
                }
            },
        )
        return True

    def find_cart(self, user_id):
        return self.database["shopping_cart"].find_one({"user_id": user_id}, {"_id": 0})

    def remove_product(self, produto_id: str, user_id: str):
        return self.database["shopping_cart"].update_one(
            {"user_id": user_id},
            {"$pull": {"itens_cart": {"product.id": produto_id}}},
        )

    def edit_quantity_product(self, user_id: str, data: dict):
        return self.database["shopping_cart"].update_one(
            {"user_id": user_id, "itens_cart.product.id": data.get("product_id")},
            {"$set": {"itens_cart.$.quantity": data.get("quantity", 0)}},
        )

    def calculate_total_product(self, data: dict) -> float:
        return data.get("product", {}).get("price", 0) * data.get("quantity", 1)
