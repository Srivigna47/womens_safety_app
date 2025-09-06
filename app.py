import streamlit as st
from twilio.rest import Client
from dotenv import load_dotenv
import os

# Load environment variables from .env (local) or Streamlit Cloud secrets
load_dotenv()

st.set_page_config(page_title="Women's Safety App", page_icon="🚨", layout="centered")

st.title("🚨 Women's Safety App")
st.write("Send an emergency WhatsApp SOS message to your trusted contacts.")

# Twilio credentials (loaded from env variables)
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH = os.getenv("TWILIO_AUTH")
TWILIO_WHATSAPP = "whatsapp:+14155238886"   # Twilio Sandbox Number

# Emergency contacts
contacts = [
    "whatsapp:+918317665051",  # Replace with real number
    "whatsapp:+918897119368"   # Replace with real number
]

# Initialize Twilio client
client = Client(TWILIO_SID, TWILIO_AUTH)

# SOS message input
sos_message = st.text_area(
    "✍️ Write your SOS message:",
    "🚨 SOS! I need help urgently. 📍 Location: https://maps.google.com/"
)

# Send SOS button
if st.button("📩 Send SOS to All"):
    for number in contacts:
        try:
            message = client.messages.create(
                body=sos_message,
                from_=TWILIO_WHATSAPP,
                to=number
            )
            st.success(f"✅ SOS sent to {number}! SID: {message.sid}")
        except Exception as e:
            st.error(f"❌ Failed to send SOS to {number}: {e}")
