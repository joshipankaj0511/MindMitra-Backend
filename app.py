import os
import google.generativeai as genai
from flask import Flask, request
from twilio.rest import Client
from emotionDetection import detect_emotion
from relaxation import get_relaxation_tips
from motivation import get_motivational_quote
from journaling import get_response
from selfcare import get_selfcare_tip
from sos import get_sos_resources
from mood_tracker import get_mood_response
#from mood_tracking import track_mood
from conversation_history import add_to_history, get_history
from meditation import get_meditation_guide
from helpers import detect_emergency
from storeUser_moods import track_mood,get_mood_history
from dotenv import load_dotenv
import logging

# Setup Logging
logging.basicConfig(
    filename="chatbot_logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logging.info("Chatbot server started!")

# Load .env file
load_dotenv()

# Environment variables ko access karo
genai_api_key = os.getenv("GEMINI_API_KEY")
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER")

# Configure Gemini API
genai.configure(api_key=genai_api_key)

# Twilio Client
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# Flask App
app = Flask(__name__)


def detect_meditation_request(user_message):
    """Detects if user is requesting meditation help."""
    meditation_keywords = ["meditate", "relax", "calm", "peaceful", "deep breath"]
    return any(word in user_message.lower() for word in meditation_keywords)

def split_message(message, limit=1600):
    """Splits messages that exceed WhatsApp character limits."""
    parts = []
    while len(message) > limit:
        split_index = message[:limit].rfind(" ")
        if split_index == -1:
            split_index = limit
        parts.append(message[:split_index])
        message = message[split_index:]
    parts.append(message)
    return parts

def get_gemini_response(user_message):
    """Fetches AI response from Google Gemini API."""

    greetings = {"hello", "hi", "hey", "namaste", "good morning", "good evening"}
    
    if user_message.lower() in greetings:
        return (
            "Hello! I'm your AI Mental Health Assistant. "
            "I'm here to listen and support you. "
            "How are you feeling today? "
        )
    
    if detect_emotion(user_message):
        return detect_emotion(user_message)

    keywords_response_map = {
        ("stress", "anxiety", "panic", "depressed"): get_relaxation_tips,
        ("sad", "hopeless", "failure", "tired"): get_motivational_quote,
        ("anxious", "confused", "stressed", "overwhelmed", "worried"): lambda: get_response(user_message),
        ("self-care", "burnout", "exhausted", "energy", "overworked"): get_selfcare_tip,
        ("help", "emergency", "suicide", "urgent", "crisis", "sos"): get_sos_resources,
        ("how are you", "mood"): lambda: "Aapka mood kaisa hai? 😊 (happy, sad, stressed, anxious, angry)",
    }
    user_words = set(user_message.lower().split())  # ✅ Fast lookup using set

    for keywords, response in keywords_response_map.items():
        if set(keywords) & user_words:  # ✅ O(n) instead of O(n^2)
            return response()

    if user_message.lower() in ["happy", "sad", "stressed", "anxious", "angry"]:
        return get_mood_response(user_message.lower())

    if "motivate me" in user_message.lower() or "inspire me" in user_message.lower():
        return get_motivational_quote()

    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(user_message)
        return response.text.strip() if response.text else "I'm here to help, but I didn’t quite get that."
    except Exception as e:
        logging.error(f"AI Error: {e}")
        return "Sorry, I couldn't process your request right now. Try again later."

@app.route('/whatsapp', methods=['POST'])
def whatsapp_reply():
    """Handles incoming WhatsApp messages and replies."""
    incoming_msg = request.values.get("Body", "").lower()
    sender_number = request.values.get("From")
    logging.info(f"Received message from {sender_number}: {incoming_msg}")

    if detect_emergency(incoming_msg):
        emergency_message = (
            "I'm really sorry you're feeling this way. 💙 Please reach out to someone you trust. "
            "For urgent help, contact iCall (Mental Health Support) 📞: +91 9152987821 "
            "or visit https://icallhelpline.org/"
        )
        client.messages.create(
            from_=TWILIO_WHATSAPP_NUMBER,
            body=emergency_message,
            to=sender_number,
        )
        return "Emergency support message sent!", 200

    if detect_meditation_request(incoming_msg):
        meditation_info = get_meditation_guide()
        client.messages.create(
            from_=TWILIO_WHATSAPP_NUMBER,
            body=meditation_info["text"],
            to=sender_number,
        )
        client.messages.create(
            from_=TWILIO_WHATSAPP_NUMBER,
            body=f"🎧 Listen to this guided meditation: {meditation_info['audio']}",
            to=sender_number,
        )
        return "Meditation guide sent!", 200

    add_to_history(sender_number, incoming_msg, "user")

    try:
        ai_response = get_gemini_response(incoming_msg)
    except Exception as e:
        logging.error(f"AI Error: {e}")
        ai_response = "Sorry, I am having some trouble understanding that."

    logging.info(f"AI Response: {ai_response}")

    add_to_history(sender_number, ai_response, "assistant")

    # Track and get the mood from MongoDB
    mood_response = get_mood_history(sender_number)  # Fetch user's mood from MongoDB
    track_mood(sender_number, incoming_msg)  # Update mood based on new message

    final_response = f"{ai_response}" if mood_response else ai_response

    for part in split_message(final_response):
        client.messages.create(
            from_=TWILIO_WHATSAPP_NUMBER,
            body=part,
            to=sender_number,
        )

    return "Message sent!", 200

if __name__ == '__main__':
    app.run(debug=True)
