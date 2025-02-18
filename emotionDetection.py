def detect_emotion(user_message):
    sad_words=["sad","depression","hopeless","alone","tired"]
    anxiety_words=["anxiety","stress","worried","panic"]
    happy_words=["happy","excited","joy","grateful"]

    for word in sad_words:
        if word in user_message.lower():
            return "what happened to you please tell me,i will try to help you."
    for word in anxiety_words:
        if word in user_message.lower(): 
            return "take some deep breathe." 
    for word in happy_words:
        if word in user_message.lower(): 
            return "i am glad to hear that.have a wonderful day." 
    return None     #default AI response