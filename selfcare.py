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
        "🍎 Healthy snacks khayiye, aapka energy level better rahega.",
        "🌿 Nature ke kareeb jayein, yeh aapko refresh karega.",
        "📝 Apne thoughts ko likhiye, yeh aapko clarity dega.",
        "📞 Kisi dost ya family member se baat karein, aapko acha lagega.",
        "🎨 Kuch creative karein, jaise drawing ya painting.",
        "🏋️‍♂️ Thoda exercise karein, yeh aapke mood ko uplift karega.",
        "🛀 Ek relaxing bath lein, yeh aapko rejuvenate karega.",
        "🌞 Thoda sunlight mein time spend karein, vitamin D zaroori hai.",
        "🍵 Ek cup green tea ya herbal tea enjoy karein, yeh aapko calm karega.",
        "🧩 Ek puzzle ya game kheliye, yeh aapke mind ko engage rakhega.",
        "📺 Apna favorite show ya movie dekhiye, relax feel hoga.",
        "🌸 Thoda gardening karein, yeh aapko nature ke kareeb rakhega.",
        "🧴 Apne aapko pamper karein, jaise skincare routine follow karein."
    ]
    return random.choice(tips)

# Example usage
if __name__ == "__main__":
    print(get_selfcare_tip())