import json
import requests

TOKEN = "408650828:AAGhRkEh_T28W2Lm2o0T-ECXf9fJy7dBpZY"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates():
    url = URL + "getUpdates"
    js = get_json_from_url(url)
    return js


def get_chat_id(updates):
    ids = []
    for i in range(len(updates["result"])):
        chat_id = updates["result"][i]["message"]["chat"]["id"]
        ids.append(chat_id)
    return ids


def send_message(text, chat_id):
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)

def send_message_all(text):
    ids = get_chat_id(get_updates())
    for chat_id in ids:
        send_message(text, chat_id)


send_message_all("Bonjour")
