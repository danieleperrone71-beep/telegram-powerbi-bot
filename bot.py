from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("TELEGRAM_TOKEN")

@app.route("/")
def home():
    return "Bot Telegram attivo!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    message = data.get("message", {}).get("text", "")
    chat_id = data.get("message", {}).get("chat", {}).get("id", "")

    if message == "/start":
        text = "✅ Bot Telegram è attivo!"
    else:
        text = f"Hai scritto: {message}"

    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={"chat_id": chat_id, "text": text}
    )
    return "ok"
