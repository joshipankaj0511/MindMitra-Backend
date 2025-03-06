import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()  # Load environment variables

MONGO_URI = os.getenv("MONGO_URI")  # MongoDB URI from .env file
client = MongoClient(MONGO_URI)
db = client["MindMitra"]  # Database Name
users = db["users"]  # Users Collection
