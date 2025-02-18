import time

# Dictionary to store user conversation history
conversation_data = {}

def add_to_history(user_id, message, role="user"):
    """Add messages to conversation history for a specific user"""
    if user_id not in conversation_data:
        conversation_data[user_id] = []

    conversation_data[user_id].append({"role": role, "content": message, "timestamp": time.time()})

    # Keep only last 10 messages for memory optimization
    if len(conversation_data[user_id]) > 10:
        conversation_data[user_id].pop(0)

def get_history(user_id):
    """Retrieve past conversation history of a user"""
    return conversation_data.get(user_id, [])
