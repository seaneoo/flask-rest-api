from pymongo.mongo_client import MongoClient
from ..config import MONGO_DB_CONNECTION_STR


class DatabaseManager:
    def __init__(self):
        self.client: MongoClient | None = None

    def connect(self):
        if MONGO_DB_CONNECTION_STR:
            self.client = MongoClient(MONGO_DB_CONNECTION_STR)
        return self

    def close(self):
        if self.client:
            self.client.close()

    def database(self):
        if self.client:
            return self.client['upcomingmcu']

    def collection(self):
        if self.client and self.database() is not None:
            return self.database()['productions_v2']
