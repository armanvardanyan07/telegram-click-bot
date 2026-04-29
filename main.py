from flask import Flask
import telebot
from threading import Thread
app = Flask(__name__)
bot = telebot.TeleBot("")
users = set()

@bot.message_handler(commands=["start"])
def start(message):
    users.add(message.chat.id)

@app.route("/click")
def click():
    for user_id in users:
        bot.send_message(user_id, "Button was pressed")
    return "ok"
if __name__ == "__main__":
    Thread(target=bot.infinity_polling, daemon=True).start()
    app.run()
