from pymongo import MongoClient, errors
from datetime import datetime  # for timestamp
import os
import logging

# Connect to MongoDB
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")  # Update with actual URI
if not MONGO_URI:
    logging.error("MONGO_URI environment variable is missing.")
    raise EnvironmentError("MONGO_URI environment variable is missing.")

try:
    client = MongoClient(MONGO_URI)
    db = client["mental_health_db"]
    moods_collection = db["user_moods"]
    logging.info("Connected to MongoDB successfully.")
except errors.ConnectionError as e:
    logging.error(f"Failed to connect to MongoDB: {e}")
    raise

def track_mood(user_id, mood):
    """Stores user mood in MongoDB with timestamp."""
    try:
        moods_collection.insert_one(
            {"user_id": user_id, "mood": mood, "timestamp": datetime.now()}
        )
        logging.info(f"Mood tracked for user {user_id}: {mood}")
    except errors.PyMongoError as e:
        logging.error(f"Failed to track mood for user {user_id}: {e}")

def get_mood_history(user_id):
    """Retrieves the user's mood history."""
    try:
        mood_history = moods_collection.find({"user_id": user_id}).sort("timestamp", 1)  # Sort by timestamp
        logging.info(f"Retrieved mood history for user {user_id}")
        return list(mood_history)
    except errors.PyMongoError as e:
        logging.error(f"Failed to retrieve mood history for user {user_id}: {e}")
        return []

def get_latest_mood(user_id):
    """Retrieves the user's latest mood."""
    try:
        latest_mood = moods_collection.find({"user_id": user_id}).sort("timestamp", -1).limit(1)
        logging.info(f"Retrieved latest mood for user {user_id}")
        return latest_mood[0] if latest_mood.count() > 0 else None
    except errors.PyMongoError as e:
        logging.error(f"Failed to retrieve latest mood for user {user_id}: {e}")
        return None

def delete_mood_history(user_id):
    """Deletes the user's mood history."""
    try:
        result = moods_collection.delete_many({"user_id": user_id})
        logging.info(f"Deleted {result.deleted_count} mood records for user {user_id}")
    except errors.PyMongoError as e:
        logging.error(f"Failed to delete mood history for user {user_id}: {e}")

# Example usage
if __name__ == "__main__":
    user_id = "user123"
    track_mood(user_id, "happy")
    track_mood(user_id, "sad")
    mood_history = get_mood_history(user_id)
    for record in mood_history:
        print(record)
    latest_mood = get_latest_mood(user_id)
    print(f"Latest mood: {latest_mood}")
    delete_mood_history(user_id)
    print(f"Mood history after deletion: {get_mood_history(user_id)}")