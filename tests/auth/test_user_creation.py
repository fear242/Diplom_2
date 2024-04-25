import pytest
import requests
import allure


URL_register = 'https://stellarburgers.nomoreparties.site/api/auth/register'
URL_user = 'https://stellarburgers.nomoreparties.site/api/auth/user'


class TestUserCreation:

    def test_register_new_user(self, generate_and_return_login_password_without_registration):

        payload = generate_and_return_login_password_without_registration
        response = requests.post(URL_register, data=payload)

        assert response.status_code == 200
        assert 'accessToken' in response.text
        requests.delete(URL_user, headers={'authorization': response.json()["accessToken"]})

    def test_register_similar_user(self, register_user_and_return_its_data):

        payload = register_user_and_return_its_data
        response = requests.post(URL_register, data=payload)

        assert response.status_code == 403
        assert response.text == '{"success":false,"message":"User already exists"}'

    @pytest.mark.parametrize('value', ["email", "password", "name"])
    def test_register_user_with_missing_data(self, generate_and_return_login_password_without_registration, value):

        payload = generate_and_return_login_password_without_registration
        payload[value] = ""
        response = requests.post(URL_register, data=payload)

        assert response.status_code == 403
        assert response.text == '{"success":false,"message":"Email, password and name are required fields"}'
