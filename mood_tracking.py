from collections import deque

# Maximum kitne past messages store karne hain
MAX_HISTORY = 5  

def track_mood(user_number, message, user_moods):
    """
    Yeh function user ke mood ko track karega aur detect karega 
    ki user kis tarah feel kar raha hai: sad, anxious, happy, ya neutral.

    Parameters:
        user_number (str): WhatsApp ya kisi bhi platform ka unique user ID.
        message (str): User ka message jo analyze kiya jayega.
        user_moods (dict): Ek dictionary jo user ke mood history ko store karega.

    Returns:
        str ya None: Agar user kuch time se same mood me hai, toh ek special response milega.
        Agar mood fluctuate ho raha hai, toh kuch nahi return hoga (None).
    """

    # Mood detect karne ke liye keywords ka ek set define kar rahe hain.
    sad_words = {"sad", "depressed", "alone", "hopeless", "unhappy"}
    anxiety_words = {"anxiety", "stress", "worried", "panic", "nervous"}
    happy_words = {"happy", "joy", "excited", "grateful", "cheerful"}

    # **Agar naye user ka data nahi hai, toh ek queue initialize karo**
    if user_number not in user_moods:
        user_moods[user_number] = deque(maxlen=MAX_HISTORY)  # Sirf last 5 moods store honge

    # **Message ko lowercase me convert karo taaki case-sensitive na ho**
    if isinstance(message, list):  # Kabhi kabhi error hota hai jab message list aa jata hai
        message = " ".join(message)  # List ke words ko ek string me convert karna
    message = message.lower()  # Sab words ko lowercase me convert karna

    # **Mood detect karo**
    mood = "neutral"  # Default mood neutral hai
    if any(word in message for word in sad_words):  # Agar sad words present hain
        mood = "sad"
    elif any(word in message for word in anxiety_words):  # Agar anxiety ke words hain
        mood = "anxious"
    elif any(word in message for word in happy_words):  # Agar happy words hain
        mood = "happy"

    # **User ke mood history me naye mood ko add karo**
    user_moods[user_number].append(mood)

    # **Mood count dictionary banayenge taaki dekha ja sake kaunsa mood frequent hai**
    mood_counts = {"sad": 0, "anxious": 0, "happy": 0, "neutral": 0}
    
    for past_mood in user_moods[user_number]:  # User ki last 5 moods ko count karo
        mood_counts[past_mood] += 1


    # **Agar user last 3-5 messages se sad/anxious/happy hai, toh special response bhejo**
    if mood_counts["sad"] >= 3:
        user_moods[user_number].clear()  # Mood history reset kar do taaki spam na ho
        return "It looks like you've been feeling down lately. I'm here for you. Maybe talking to a friend or taking a walk could help?"
    
    elif mood_counts["anxious"] >= 3:
        user_moods[user_number].clear()
        return "You've been feeling anxious for a while. Try some breathing exercises or a short meditation. Let me know if I can help!"
    
    elif mood_counts["happy"] >= 3:
        user_moods[user_number].clear()
        return "I'm glad to see that you're feeling happy! Keep spreading positivity! 😊"

    return None  # **Agar koi special mood pattern detect nahi hota, toh kuch nahi bhejo**

    

