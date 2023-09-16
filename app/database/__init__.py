from pymongo.mongo_client import MongoClient
from ..config import MONGO_DB_CONNECTION_STR

client = MongoClient(MONGO_DB_CONNECTION_STR)
db = client['upcomingmcu']
col = db['productions_v2']


def close():
    client.close()
