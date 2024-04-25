import pytest
import requests
import allure
from faker import Faker


fake = Faker(['ru_RU'])
URL_login = 'https://stellarburgers.nomoreparties.site/api/auth/login'
URL_user = 'https://stellarburgers.nomoreparties.site/api/auth/user'

class TestUserChange:

    @pytest.mark.parametrize('value', ["email", "password", "name"])
    def test_change_authorised_user(self, register_user_and_return_its_data, value):
        payload = register_user_and_return_its_data
        resp = requests.post(URL_login, data=payload)
        token = resp.json()["accessToken"]
        value = fake.name()
        response = requests.patch(URL_user, data=value, headers={'authorization': token})
        assert response.status_code == 200
        assert '"success":true' in response.text

    @pytest.mark.parametrize('value', ["email", "password", "name"])
    def test_change_non_authorised_user(self, register_user_and_return_its_data, value):
        value = fake.name()
        response = requests.patch(URL_user, data=value)
        assert response.status_code == 401
        assert response.text == '{"success":false,"message":"You should be authorised"}'
