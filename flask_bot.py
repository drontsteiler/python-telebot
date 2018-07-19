import os
import spacy
import store
import telebot
import google_place_api
import main
from flask import Flask, request

TOKEN = store.token
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

print(bot.get_me())


####################################

@bot.message_handler(commands=["start"])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('/start', '/stop')
    bot.send_message(message.from_user.id, "Welcome, " + message.from_user.first_name, reply_markup=user_markup)


@bot.message_handler(commands=["stop"])
def handle_start(message):
    hide_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, "..", reply_markup=hide_markup)


@bot.message_handler(content_types="text")
def handle_text(message):
    #bot.send_message(message.chat.id, main.weatherapp(message.text), parse_mode="HTML")
    msg = "error"
    msg = main.weatherapp(message.text)
    bot.send_message(message.chat.id, msg, parse_mode = "HTML")


#######################################

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
