import pytest
import requests
import helper
import allure
from data import DataLinks


@allure.title('Регистрация нового пользователя и возврат его учётных данных')
@pytest.fixture()
def register_user_and_return_its_data():
    payload = helper.generate_and_return_login_password_without_registration()
    response = requests.post(DataLinks.URL_register, data=payload)
    yield payload
    requests.delete(DataLinks.URL_user, headers={'authorization': response.json()["accessToken"]})
