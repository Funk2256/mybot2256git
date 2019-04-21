# -*- coding: utf-8 -*-
import config
import telebot
from telebot import types
from telebot import apihelper
import os



apihelper.proxy = {'https':'socks5://userid10Oh:mlLbfK@185.36.191.39:7992'}

bot = telebot.TeleBot(config.token)

# Обработчик команд '/start' и '/help'.
@bot.message_handler(commands=['start', 'help', 'keyboard'])
def handle_start_help(message):
    pass

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)


port=int(os.environ.get('PORT', 5000)


"""markup = types.ReplyKeyboardMarkup()
markup.row('a', 'v')
markup.row('c', 'd', 'e')

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
	bot.send_message(message.chat.id, "Choose one letter:", reply_markup=markup)
"""
if __name__ == '__main__':
     bot.polling(none_stop=True)