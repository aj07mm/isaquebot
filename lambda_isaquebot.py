# coding: utf-8
import json
from botocore.vendored import requests

TELE_TOKEN='<TELE_TOKEN>'
URL = "https://api.telegram.org/bot{}/".format(TELE_TOKEN)

def send_message(text, chat_id):
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    requests.get(url)

def lambda_handler(event, context):
    message = json.loads(event['body'])
    chat_id = message['message']['chat']['id']
    text = message['message']['text']
    reply = None
    if "sergio" in text:
        reply = 'Vamo fuma droga na casa do Sergio'
    elif "maconha" in text:
        reply = 'Onde?'
    elif "biome" in text:
        reply = 'Biome 🎵Baaa Biomee 🎶'
    elif "mahalila" in text:
        reply = 'Vamo pro mahalila'
    elif "laluna" in text:
        reply = 'Vamo pro laluna'
    if reply:
        send_message(reply, chat_id)
    return {
        'statusCode': 200
    }
