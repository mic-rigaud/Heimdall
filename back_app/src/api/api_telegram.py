import json
import requests
import logging

#TOKEN = "408650828:AAGhRkEh_T28W2Lm2o0T-ECXf9fJy7dBpZY"
#URL = "https://api.telegram.org/bot{}/".format(TOKEN)

class ApiTelegram():
    URL = ""

    def __init__(self, token):
        self.URL = "https://api.telegram.org/bot{}/".format(token)

    def get_url(self, url):
        response = requests.get(url)
        content = response.content.decode("utf8")
        return content

    def get_json_from_url(self, url):
        content = self.get_url(url)
        js = json.loads(content)
        return js

    def get_updates(self):
        url = self.URL + "getUpdates"
        js = self.get_json_from_url(url)
        return js

    def get_chat_id(self, updates):
        ids = []
        for i in range(len(updates["result"])):
            chat_id = updates["result"][i]["message"]["chat"]["id"]
            ids.append(chat_id)
        return ids

    def send_message(self, text, chat_id):
        url = self.URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
        self.get_url(url)

    def send_message_all(self, text):
        ids = self.get_chat_id(self.get_updates())
        if not ids:
            logging.warning("Aucun peripherique connecte au bot telegram")
        for chat_id in ids:
            self.send_message(text, chat_id)

    def send_alert(self, text):
        logging.warning("Envoie de l alerte via telegram : {}".format(text))
        alerte = "-- BLUEBERRY : ALERTE-- \n{} \n----".format(text)
        self.send_message_all(alerte)
