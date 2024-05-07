import random
import string
import allure
from faker import Faker

fake = Faker(['ru_RU'])


@allure.title('Генерация строки из 10 случайных букв нижнего регистра')
def generate_random_string():
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(10))
    return random_string


@allure.title('Генерация и возврат учётных данных пользователя')
def generate_and_return_login_password_without_registration():
    email = fake.email()
    password = fake.password()
    name = fake.name()

    payload = {
        "email": email,
        "password": password,
        "name": name
    }
    return payload
