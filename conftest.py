import pytest
import random
import string
import requests
import allure
from faker import Faker


fake = Faker(['ru_RU'])
URL_register = 'https://stellarburgers.nomoreparties.site/api/auth/register'
URL_user = 'https://stellarburgers.nomoreparties.site/api/auth/user'


@allure.title('Генерация строки из 10 случайных букв нижнего регистра')
@pytest.fixture()
def generate_random_string():
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(10))
    return random_string


@allure.title('Генерация и возврат учётных данных пользователя')
@pytest.fixture()
def generate_and_return_login_password_without_registration(generate_random_string):
    email = fake.email()
    password = generate_random_string
    name = fake.name()

    payload = {
        "email": email,
        "password": password,
        "name": name
    }
    return payload


@allure.title('Регистрация нового пользователя и возврат его учётных данных')
@pytest.fixture()
def register_user_and_return_its_data(generate_and_return_login_password_without_registration):
    payload = generate_and_return_login_password_without_registration
    response = requests.post(URL_register, data=payload)
    if response.status_code == 200:
        yield payload
    requests.delete(URL_user, headers={'authorization': response.json()["accessToken"]})
