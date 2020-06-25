import telebot
bot = telebot.TeleBot('1173534227:AAEyY_bealeUXZwj7_ads2w8EKWjLTYwtt8')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "Как дела?":
        bot.send_message(message.from_user.id, "отлично")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
bot.polling(none_stop=True, interval=0)
