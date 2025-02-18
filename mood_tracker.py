def get_mood_response(user_mood):
    mood_responses = {
        "happy": "😊 Bohot accha! Aap khush hain, yeh sun kar acha laga! Apni positivity share karein. ❤️",
        "sad": "😔 Koi baat nahi, sab theek ho jayega. Aapke liye relaxation tips bhej raha hoon.",
        "stressed": "😟 Stress normal hai, lekin apna khayal rakhna zaroori hai. Chaliye kuch relaxation techniques try karein!",
        "anxious": "😰 Agar aap tension me hain toh deep breathing aur meditation zaroori hai.",
        "angry": "😡 Gussa aana normal hai, lekin usko control karna bhi zaroori hai. Relaxation techniques try karein."
    }

    return mood_responses.get(user_mood.lower(), "Aap ka mood samajh nahi aaya. Aap thoda aur detail me bata sakte hain?")  
