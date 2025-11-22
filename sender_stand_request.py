import requests
from configuration import URL_SERVICE, CREATE_USER_PATH, CREATE_KIT_PATH

def post_new_user(body):
    """
    Создаёт нового пользователя и возвращает ответ.
    """
    return requests.post(URL_SERVICE + CREATE_USER_PATH, json=body)

def get_new_user_token():
    """
    Создаёт пользователя и возвращает authToken из ответа.
    """
    user_body = {
        "firstName": "Анатолий",
        "phone": "+77771234567",
        "address": "Астана"
    }

    response = post_new_user(user_body)
    auth_token = response.json()["authToken"]
    return auth_token

def post_new_kit(body, auth_token):
    """
    Создаёт новый набор (kit) c заголовком Authorization.
    """
    headers = {
        "Authorization": auth_token
    }

    return requests.post(URL_SERVICE + CREATE_KIT_PATH, headers=headers, json=body)