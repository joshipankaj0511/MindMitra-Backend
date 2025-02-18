import random

def get_selfcare_tip():
    tips = [
        "🚶‍♂️ Aaj thoda walk par jayein, fresh air aapko relax karegi.",
        "🛌 Thoda araam karein, ek achhi neend lena zaroori hai!",
        "📖 Ek interesting book padhiye, yeh aapke dimaag ko relax karega.",
        "🧘‍♀️ 5-minute deep breathing exercise karein, stress kam hoga.",
        "🎵 Apni favorite music suniye, mood better ho jayega! 🎶",
        "📅 Thoda time apne liye rakhein, hobbies par dhyan dein.",
        "💧 Pani peena na bhooliye, dehydration bhi thakan badhata hai!",
    ]
    return random.choice(tips)
