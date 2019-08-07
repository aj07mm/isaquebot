# coding: utf-8
import os
import telebot

bot = telebot.TeleBot(os.environ.get("ISAQUEBOT_TOKEN"))

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

def handle_messages(messages):
    for message in messages:
        if "sergio" in message.text or "Sergio" in message.text:
            bot.reply_to(message, 'Vamo fuma droga na casa do Sergio')
        if "maconha" in message.text:
            bot.reply_to(message, 'Onde?')

bot.set_update_listener(handle_messages)


bot.polling()
