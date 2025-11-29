import requests
import random

BOT_TOKEN = "8263436435:AAEODCFDQH3EkBEjsy4uJZeIAFqsRwFCR58"
CHAT_ID = "1709893544"

quotes = [
    "SSC CGL is not just an exam, it's a battle for your dream post. Get back to work!",
    "Imagine the uniform. Imagine the respect. An Income Tax Inspector doesn't sleep on their goals.",
    "Maths needs practice, not excuses. Solve 10 more questions right now.",
    "The competition is studying while you are distracted. Focus!",
    "General Awareness is vast, but your will is stronger. Read one topic now.",
    "Don't stop until you get that government stamp on your appointment letter.",
    "Mock test scores low? Analyze it. Don't quit. Improve.",
    "30 minutes passed. Did you make them count? The next 30 are yours.",
    "Reasoning is all about speed. Pick up the pace!",
    "Consistency beats intensity. Just keep going."
]

def send_message():
    msg = random.choice(quotes)
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": "🔔 CGL ALERT 🔥\n\n" + msg}
    requests.post(url, data=data)

send_message()
