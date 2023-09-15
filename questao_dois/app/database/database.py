from app import settings
from pymongo import MongoClient


class DBConnection:
    def __init__(self) -> None:
        self.client = MongoClient(settings.MONGO_URL)
        self.database = self.client[settings.DATABASE_ENVIRONMENT]

