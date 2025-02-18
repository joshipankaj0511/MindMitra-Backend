def detect_emergency(message):
    emergency_keywords = ["suicide", "self harm", "want to die", "depressed", "ending life", "no hope", "kill myself"]
    
    for word in emergency_keywords:
        if word in message:
            return True
    return False
