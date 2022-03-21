import json
import os

import requests
from telegram import KeyboardButton, ReplyKeyboardMarkup

WEATHER_BOT_TOKEN = os.environ.get('weather_bot_token')
BOT_URL = "https://api.telegram.org/bot{}/".format(WEATHER_BOT_TOKEN)

weather_keyboard = [
    [KeyboardButton("Today", request_location=True),
     KeyboardButton("Forecast 7", request_location=True)],
    [KeyboardButton("Today By City"),
     KeyboardButton("Forecast By City")],
]


def prepare_message_text(data):
    message = "<b>Location:</b> " + data['location'] + "\n Region: " + data['region']
    return message


def send_message_get(message, chat_id):
    print('Sending reply to bot: ', message, ' chatid: ', chat_id)

    reply_message = "<b>Location:</b> " + message['location']['name'] + ", " + message['location']['region'] + ', ' + \
                    message['location']['country']
    reply_message = reply_message + "\n" + "<b>Time and Zone: </b>" + message['location']['localtime'] + ', ' + \
                    message['location'][
                        'tz_id']
    reply_message = reply_message + "\n" + "<b>Temperature: </b>" + message['current']['condition'][
        'text'] + ", " + str(
        message['current'][
            'temp_c']) + 'C / ' + str(message['current']['temp_f']) + 'F'

    url = BOT_URL + "sendMessage?text={}&chat_id={}&parse_mode=HTML".format(reply_message, chat_id)
    resp = requests.get(url)
    print('Response from bot: ', resp.json())


def send_message_post(chat_id, data):
    print('Sending reply  keyboard to bot')
    url = BOT_URL + "sendMessage?parse_mode=HTML"
    reply_data = {
        "chat_id": chat_id,
        "text": 'Choose an option from keyboard menu',
        "reply_markup": json.dumps(data.to_dict())
    }
    resp = requests.post(url, data=data)
    print('query response: ', resp.json())


def sent_start_keyboard(chat_id):
    new_markup = ReplyKeyboardMarkup(weather_keyboard, resize_keyboard=True)
    data = {
        "chat_id": chat_id,
        "text": 'Choose an option from keyboard menu',
        "reply_markup": json.dumps(new_markup.to_dict())
    }
    send_message_post(data)
