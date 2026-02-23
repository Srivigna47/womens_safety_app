import streamlit as st
import urllib.parse

st.set_page_config(page_title="Women's Safety App")

st.title("🚨 Women's Safety App")

st.write("Tap the button below to send SOS to emergency contacts.")

# 🔴 ADD YOUR EMERGENCY CONTACT NUMBERS HERE
phone_numbers = "8317665051,8897119368,9701523021"

message = "🚨 SOS! I am in danger. Please help me immediately."

encoded_message = urllib.parse.quote(message)

sms_link = f"sms:{phone_numbers}?body={encoded_message}"

st.markdown(f"""
<a href="{sms_link}">
    <button style="
        background-color:red;
        color:white;
        padding:20px;
        font-size:22px;
        border-radius:12px;
        border:none;
        width:100%;">
        🚨 SEND SOS
    </button>
</a>
""", unsafe_allow_html=True)