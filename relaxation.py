import random

def get_relaxation_tips():
    relaxation_tips = [
        "Deep breathing exercise karein: 4 seconds tak saans andar lein, 4 seconds tak rokein, aur 4 seconds tak saans bahar chhod dein. Yeh cycle 5 baar repeat karein. 😊",
        "Ek sukoon bhari jagah par baithiye, aankhein band karke dhyan lagaiye aur apni saans par focus karein. Yeh aapko shanti dega. 🧘‍♂️",
        "Relaxing music ya nature sounds sunne ki koshish karein. Yeh aapke mind ko calm karega. 🎶",
        "Ek lambe walk par jaaiye ya halka phulka exercise karein. Physical activity aapke stress levels ko kam kar sakti hai. 🚶‍♀️",
        "Apni pasandida kitaab padhein ya likhne ki aadat daaliye. Writing helps in reducing stress. 📖✍️",
        "Aromatherapy try karein, jaise lavender ya chamomile essential oils ka use karein. Yeh aapko relax karne mein madad karega. 🌸",
        "Meditation karein, yeh aapke mind ko calm aur focused rakhega. 🧘‍♀️",
        "Ek cup herbal tea enjoy karein, jaise chamomile ya peppermint tea. 🍵",
        "Thoda stretching exercise karein, yeh aapke muscles ko relax karega. 🧘‍♂️",
        "Ek warm bath lein, yeh aapko rejuvenate karega. 🛀",
        "Apne pet ke saath time spend karein, yeh aapko instantly happy aur relaxed feel karayega. 🐶🐱",
        "Thoda gardening karein, yeh aapko nature ke kareeb rakhega aur mind ko fresh karega. 🌿",
        "Apne favorite movie ya show dekhiye, yeh aapko entertain aur relax karega. 📺",
        "Kuch creative karein, jaise painting, drawing ya crafting. 🎨",
        "Ek gratitude journal maintain karein, yeh aapko positive aur grateful feel karayega. 📝"
    ]
    return random.choice(relaxation_tips)

# Example usage
if __name__ == "__main__":
    print(get_relaxation_tips())