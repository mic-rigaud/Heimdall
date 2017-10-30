import json
import requests
import logging


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
        try:
            js = json.loads(content)
        except:
            logging.error("La réponse recut par l api telegram n'est pas au format json")
            js = "Error"
        return js

    def get_updates(self):
        url = self.URL + "getUpdates"
        js = self.get_json_from_url(url)
        return js

    def send_message(self, text, chat_id):
        url = self.URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
        self.get_url(url)

    def send_alert(self, text, chat_id):
        logging.warning("Envoie de l alerte via telegram : {}".format(text))
        alerte = "-- BLUEBERRY : ALERTE-- \n{} \n----".format(text)
        self.send_message(alerte, chat_id)
