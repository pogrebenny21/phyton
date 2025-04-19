import telebot
import urllib.request
from telebot import types
import datetime
import os
import random

token="7717714068:AAHykzGoeewJODXkOzEglVLLXERzsd5IU9Q"
bot = telebot.TeleBot("7717714068:AAHykzGoeewJODXkOzEglVLLXERzsd5IU9Q")
now= datetime.datetime.now()

@bot.message_handler(content_types=["text"])
def dialog(message):
    if message.text=="Привет" or message.text == "":
        bot.send_message(message.chat.id,  "Добрый День")
        if message.text == "Как Настроение?":
            bot.send_message(message.chat.id, "У меня всё хорошо а у тебя?")

bot.infinity_polling()

@bot.message_handler(content_types=["text"])
def dialog(message):
    today=now.day
    hour=now.hour
    if message.text == "Привет":
        if today == now.day and 6<= hour< 12:
            bot.swnd_message(message.chat.id text: "Привествую Васю \n")