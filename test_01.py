import telebot
import store

bot = telebot.TeleBot(store.token)

print(bot.get_me())


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
    bot.send_message(message.chat.id,"""\r
    <b style='color:red'>You write to me</b>
    """, parse_mode="HTML")


bot.polling(none_stop=True, interval=1)
