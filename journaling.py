import random

def get_response(user_message):
    user_message = user_message.lower()

    if "anxious" in user_message or "stress" in user_message or "tension" in user_message:
        return random.choice([
            "Mujhe samajh aaya ki aap thoda stress me hain. Kya aap ek chhoti si deep breathing exercise try karna chahenge? 🧘‍♂️",
            "Aapke emotions valid hain. Koi specific reason hai jo aap share karna chahenge? 🤗",
            "Main samajh sakta hoon ki aap anxious feel kar rahe hain. Kya main aapko relaxation tips bataun? 🌿"
        ])
    
    elif "sad" in user_message or "depressed" in user_message:
        return random.choice([
            "Agar aap udaas mehsoos kar rahe hain, toh apni feelings kisi close friend ya family member se share karein. Aapke emotions zaroori hain. ❤️",
            "Aap akele nahi hain! Agar aap chahen toh main aapko thoda positive mindset develop karne me help kar sakta hoon. 💛"
        ])

    elif "happy" in user_message or "excited" in user_message:
        return random.choice([
            "Ye sunke accha laga! Kya aap mujhe batana chahenge ki kis wajah se aap khush hain? 😊",
            "Achi baat hai! Happiness ka celebration zaroori hai. Aapka happy moment kya tha? 🎉"
        ])
    
    else:
        return random.choice([
            "Aaj aap kis cheez ke liye grateful hain? 🙏",
            "Aapka sabse bada goal kya hai aur uske taraf kaise badh rahe hain? 🎯"
        ])

