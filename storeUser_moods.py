from pymongo import MongoClient
from datetime import datetime  # for timestamp
import os

# Connect to MongoDB
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")  # Update with actual URI
client = MongoClient(MONGO_URI)
db = client["mental_health_db"]
moods_collection = db["user_moods"]

def track_mood(user_id, mood):
    """Stores user mood in MongoDB with timestamp."""
    moods_collection.insert_one(
        {"user_id": user_id, "mood": mood, "timestamp": datetime.now()}
    )

def get_mood_history(user_id):
    """Retrieves the user's mood history."""
    mood_history = moods_collection.find({"user_id": user_id}).sort("timestamp", 1)  # Sort by timestamp
    return list(mood_history)

# Example usage
if __name__ == "__main__":
    user_id = "user123"
    track_mood(user_id, "happy")
    track_mood(user_id, "sad")
    mood_history = get_mood_history(user_id)
    for record in mood_history:
        print(record)
