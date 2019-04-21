# -*- coding: utf-8 -*-
import config
import telebot
from telebot import types
from telebot import apihelper
import os
import flask

apihelper.proxy = {'https':'socks5://userid10Oh:mlLbfK@185.36.191.39:7992'}

bot = telebot.TeleBot(config.token)

# Обработчик команд '/start' и '/help'.
@bot.message_handler(commands=['start', 'help', 'keyboard'])
def handle_start_help(message):
    pass

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)


"""markup = types.ReplyKeyboardMarkup()
markup.row('a', 'v')
markup.row('c', 'd', 'e')

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
	bot.send_message(message.chat.id, "Choose one letter:", reply_markup=markup)
"""
if __name__ == '__main__':
     bot.polling(none_stop=True)

server = flask.Flask(__name__)
 
 
@server.route('/' + TOKEN, methods=['POST'])
def get_message():
    bot.process_new_updates([types.Update.de_json(
         flask.request.stream.read().decode("utf-8"))])
    return "!", 200
 
 
@server.route('/', methods=["GET"])
def index():
    bot.remove_webhook()
    bot.set_webhook(url="https://{}.herokuapp.com/{}".format(APP_NAME, TOKEN))
    return "Hello from Heroku!", 200
 
 
if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))