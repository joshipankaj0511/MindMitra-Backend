import random

def get_motivational_quote():
    quotes = [
        "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle.",
        "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill",
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Difficulties in life are intended to make us better, not bitter.",
        "Himmat mat haaro, safalta bas ek kadam door ho sakti hai! 🚀",
        "Dream big, work hard, stay focused, and surround yourself with good people.",
        "Every day is a new beginning. Take a deep breath, smile, and start again.",
        "Zindagi ek challenge hai, lekin tum ek warrior ho! 💪🔥",
        "Your limitation—it’s only your imagination.",
        "Push yourself, because no one else is going to do it for you."
    ]
    return random.choice(quotes)

# Example usage
if __name__ == "__main__":
    print(get_motivational_quote())
