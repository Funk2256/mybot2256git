# -*- coding: utf-8 -*-
import config
import proxy
import telebot
from telebot import types
import run_server

bot = telebot.TeleBot(config.token)

# Обработчик команд '/start' и '/help'.
@bot.message_handler(commands=['start', 'help', 'keyboard'])
def handle_start_help(message):
    pass

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.polling(none_stop=True)
