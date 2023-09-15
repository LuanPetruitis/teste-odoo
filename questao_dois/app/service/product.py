from app.database.database import database


class Product:
    def __init__(self):
        self.database = database

    def create(self, product_data):
        product_exist = self.database["products"].find_one(
            {"name": product_data.get("name")}
        )
        if product_exist:
            return False

        self.database["products"].insert_one(product_data)
        return True

    def delete(self, product_id: str):
        try:
            self.database["products"].delete_one({"id": product_id})
            return True
        except ValueError:
            return False

    def edit(self, product_id: str, product_data):
        try:
            product_exist = self.database["products"].find_one(
                {"name": product_data.get("name")}
            )
            if product_exist:
                return False

            self.database["products"].update_one(
                {"id": product_id}, {"$set": product_data}
            )
            return True
        except ValueError:
            return False

    def all_products(self):
        try:
            products = list(self.database["products"].find({}, {"_id": 0}))
            return products
        except ValueError:
            return False

    def find(self, product_id: str):
        try:
            product = self.database["products"].find_one({"id": product_id}, {"_id": 0})
            return product
        except ValueError:
            return False
