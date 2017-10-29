import pytest
from application.src.api.api_telegram import *
from application.src.api.api_bdd import *


def test_get_updates():
    telegram_token = Parametre.get(Parametre.section == "telegram" , Parametre.key == "token")
    telegram_chat_id = Parametre.get(Parametre.section == "telegram" , Parametre.key == "chat_id")
    api = ApiTelegram(telegram_token)
    assert api.get_updates() != 0
