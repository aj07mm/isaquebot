# coding: utf-8
import json
import random

from botocore.vendored import requests


TELE_TOKEN = '<TELE_TOKEN>'
URL = "https://api.telegram.org/bot{}/".format(TELE_TOKEN)


def get_random():
    return random.randrange(1, 100)

def get_reply(message_text):
    random_number = get_random()
    reply = None
    if "sergio" in message_text:
        if random_number < 50:
            reply = 'Vamo fuma droga na casa do Sergio'
        else:
            reply = 'O Sergio tem maconha?'
    elif "maconha" in message_text:
        reply = 'Onde?'
    elif "lsd" in message_text:
        reply = 'Onde?'
    elif "biome" in message_text:
        if random_number < 50:
            reply = 'Biome 🎵Baaa Biomee 🎶'
        else:
            reply = 'Neurociencia cara'
    elif "mahalila" in message_text:
        reply = 'Vamo pro mahalila'
    elif "laluna" in message_text:
        reply = 'Vamo pro laluna'
    elif "ela" in message_text:
        reply = 'Sua irmã ta solteira?'
    return reply


def send_message(text, chat_id):
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    requests.get(url)


def lambda_handler(event, context):
    message = json.loads(event['body'])
    chat_id = message['message']['chat']['id']
    message_text = message['message']['text']
    reply = get_reply(message_text)
    if reply:
        send_message(reply, chat_id)
    return {
        'statusCode': 200
    }
