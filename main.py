import telebot
from telebot import types

API_KEY = "7717714068:AAHykzGoeewJODXkOzEglVLLXERzsd5IU9Q"

# pip install pyTelegramBotAPI

bot = telebot.TeleBot(API_KEY)


@bot.message_handler(content_types=["text", "sticker"])
def handle_text(message:types.Message):
    print(message)
    chat_id = message.chat.id

    if message.text == "Привет":
        bot.send_message(chat_id, "Салага Привет!")
    elif message.text == "Пока":
        bot.send_message(chat_id, "Итог Этих Игр: ГОВНО!")
        bot.send_photo(chat_id, open("./images/Снимок.PNG", "rb"))
        bot.send_sticker(chat_id, open("./images/3232.PNG"))


print("*************Включаем Бота************")
bot.infinity_polling()
