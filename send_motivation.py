import os
import time
import schedule
from twilio.rest import Client
from motivational_quotes import get_motivational_quote  # Import motivational quotes function

# Twilio Credentials (Replace with your own)
TWILIO_SID = "AC7b6f2e3aa31d97eee2e852478ac250e1"
TWILIO_AUTH_TOKEN = "f833c7d07156c61039e4571db97d0c3b"
TWILIO_WHATSAPP_NUMBER = "whatsapp:+14155238886"  # Twilio sandbox number
USER_WHATSAPP_NUMBER = "whatsapp:+91XXXXXXXXXX"  # Apna ya user ka number

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

# Function to send daily motivation
def send_daily_motivation():
    quote = get_motivational_quote()
    message = client.messages.create(
        body=f"🌟 Daily Motivation: {quote}",
        from_=TWILIO_WHATSAPP_NUMBER,
        to=USER_WHATSAPP_NUMBER
    )
    print(f"Motivational message sent: {quote} (SID: {message.sid})")

# Schedule daily message at 9 AM
schedule.every().day.at("09:00").do(send_daily_motivation)  # Change time as needed

if __name__ == "__main__":
    print("✅ Daily motivation scheduler started...")
    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every minute
