import os
import spacy
from telebot import types
import store
import telebot
import main
from flask import Flask, request

TOKEN = store.token
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)
print("_______________________________________________________________\n"
      + "Start Telegram Bot in file flask_bot.py" +
      "\n_______________________________________________________________")


########################################################################################################

@bot.message_handler(commands=["start"])
def handle_start(message):
    bot.send_message(message.from_user.id, "Welcome, " + message.from_user.first_name)


@bot.message_handler(commands=["stop"])
def handle_start(message):
    bot.send_message(message.chat.id, "..")


@bot.message_handler(content_types="text")
def handle_text(message):
    msg = "error"
    print(message.text)
    if message.text == "Что ты умеешь делать?":
        keyboard = types.InlineKeyboardMarkup()
        weather = types.InlineKeyboardButton(text="Weather",  callback_data="inline")
        wikipedia = types.InlineKeyboardButton(text="Энциклопедия")
        translate = types.InlineKeyboardButton(text="Переводчик")
        currency = types.InlineKeyboardButton(text="Валюта")
        payment = types.InlineKeyboardButton(text="Платеж")
        keyboard.add(weather)
        bot.send_message(message.chat.id, "Я могу делать следующие:", reply_markup=keyboard)
    else:
        msg = main.weatherapp(message.text)
        bot.send_message(message.chat.id, msg, parse_mode="HTML")


############################################################################################################################

@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://ramazan-telebot-test.herokuapp.com/' + TOKEN)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
