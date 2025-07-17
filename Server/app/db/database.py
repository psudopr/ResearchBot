from pymongo import MongoClient
from app.core.config import Config

client = MongoClient(Config.MONGO_URI)
db = client[Config.DB_NAME]
