from pymongo import MongoClient
from app.config.settings import Config

client = MongoClient(Config.MONGO_URI)

mongo_db = client["oracle_raw"]

rss_collection = mongo_db["rss_articles"]