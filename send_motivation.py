import os
import time
import schedule
import logging
from twilio.rest import Client
from motivational_quotes import get_motivational_quote  # Import motivational quotes function
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Twilio Credentials
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER")
USER_WHATSAPP_NUMBERS = os.getenv("USER_WHATSAPP_NUMBERS").split(",")  # Comma-separated list of user numbers

# Validate environment variables
if not all([TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_WHATSAPP_NUMBER, USER_WHATSAPP_NUMBERS]):
    raise EnvironmentError("One or more environment variables are missing.")

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# Setup Logging
logging.basicConfig(
    filename="motivation_logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logging.info("Motivation scheduler started!")

# Function to send daily motivation
def send_daily_motivation():
    quote = get_motivational_quote()
    for user_number in USER_WHATSAPP_NUMBERS:
        try:
            message = client.messages.create(
                body=f"🌟 Daily Motivation: {quote}",
                from_=TWILIO_WHATSAPP_NUMBER,
                to=user_number.strip()
            )
            logging.info(f"Motivational message sent to {user_number}: {quote} (SID: {message.sid})")
        except Exception as e:
            logging.error(f"Failed to send motivational message to {user_number}: {e}")

# Schedule daily message at 9 AM
schedule.every().day.at("09:00").do(send_daily_motivation)  # Change time as needed

if __name__ == "__main__":
    print("✅ Daily motivation scheduler started...")
    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every minute