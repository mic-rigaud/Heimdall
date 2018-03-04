import pytest
from application.src.api.api_telegram import *

from requests.models import Response

@pytest.mark.parametrize("error_code,data", [
    (200, '{"test" : "test"}'),
    (400, '{"test" : "test"}'),
])
def test_get_url(monkeypatch, error_code, data):
    def monkeyreturn(request):
        # Cette fonction permet de formater une reponse contenant:
        # le retour code: error_code
        # et les donnees: data
        response = Response()
        response.status_code = error_code
        response._content = data.encode('utf8')
        return response
    monkeypatch.setattr(requests, 'get', monkeyreturn)
    api = ApiTelegram("token")
    assert api.get_url("essai") == data


@pytest.mark.parametrize("error_code,data", [
    (200, '{"test" : "test"}'),
    (400, '{"test" : "test"}'),
    (404, 'Not found')
])
def test_get_json_from_url(monkeypatch, error_code, data):
    def monkeyreturn(request):
        # Cette fonction permet de formater une reponse contenant:
        # le retour code: error_code
        # et les donnees: data
        response = Response()
        response.status_code = error_code
        response._content = data.encode('utf8')
        return response
    monkeypatch.setattr(requests, 'get', monkeyreturn)
    api = ApiTelegram("token")
    if error_code == 404:
        assert api.get_json_from_url("essai") == "Error"
    else:
        assert api.get_json_from_url("essai") == json.loads(data)

@pytest.mark.parametrize("error_code,data", [
    (200, '{"test" : "test"}'),
])
def test_send_message(monkeypatch, error_code, data):
    url_expected = "https://api.telegram.org/bottoken/sendMessage?text=essai&chat_id=25555"
    def monkeyreturn(request):
        # Cette fonction permet de formater une reponse contenant:
        # le retour code: error_code
        # et les donnees: data
        response = Response()
        response.status_code = error_code
        response._content = data.encode('utf8')
        assert url_expected == request
        return response
    monkeypatch.setattr(requests, 'get', monkeyreturn)
    api = ApiTelegram("token")
    api.send_message("essai",25555)



@pytest.mark.parametrize("error_code,data", [
    (200, '{"test" : "test"}'),
])
def test_send_alert(monkeypatch, error_code, data):
    url_expected = "https://api.telegram.org/bottoken/sendMessage?text={}&chat_id=25555".format("-- BLUEBERRY : ALERTE-- \nessai \n----")
    def monkeyreturn(request):
        # Cette fonction permet de formater une reponse contenant:
        # le retour code: error_code
        # et les donnees: data
        response = Response()
        response.status_code = error_code
        response._content = data.encode('utf8')
        assert url_expected == request
        return response
    monkeypatch.setattr(requests, 'get', monkeyreturn)
    api = ApiTelegram("token")
    api.send_alert("essai",25555)
