# -*- coding: utf-8 -*-
#!/usr/bin/python3
import config
import proxy
import telebot
import run_server

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def handle_start_help(message):
	bot.reply_to(message, "This is TestBot2256")

@bot.message_handler(commands=['help'])
def handle_start_help(message):
	bot.reply_to(message, "Помоги себе сам....")

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)




if __name__ == '__main__':
     bot.polling(none_stop=True)

