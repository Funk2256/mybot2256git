# -*- coding: utf-8 -*-
#!/usr/bin/python3
import config
import proxy
import telebot
import run_server
#import certifi
#import requests

#url = 'http://api.telegram.org'
#r = requests.get(url, verify=False)

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.polling(none_stop=True)