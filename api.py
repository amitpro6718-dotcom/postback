from flask import Flask, request
import requests

app = Flask(__name__)

# ------- CONFIGURATION ------- #
BOT_TOKEN = "8329106749:AAHs-jrqXNJuRJWk9UzcMtPxOlyZ1z9Gxuc"
CHAT_ID = "@tsialerts"  # Channel username or chat ID

# ------- ROUTE TO HANDLE GET REQUEST ------- #
@app.route("/", methods=["GET"])
def postback():
    click_id   = request.args.get("click_id", "N/A")
    sub1       = request.args.get("sub1", "N/A")
    offerid    = request.args.get("offerid", "N/A")
    click_time = request.args.get("click_time", "N/A")
    timestamp  = request.args.get("timestamp", "N/A")
    source     = request.args.get("source", "N/A")

    # Create Telegram message
    message = (
        "🚀 *New Conversion Received*\n\n"
        f"🆔 Click ID: {click_id}\n"
        f"👤 Sub ID: {sub1}\n"
        f"📌 Offer ID: {offerid}\n"
        f"⏱ Click Time: {click_time}\n"
        f"📅 Conversion Time: {timestamp}\n"
        f"🌍 Source: {source}\n"
    )

    # Send to Telegram
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    requests.get(url, params=payload)

    return "OK"  # Response to offer tracker


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
