import pytest
import requests
import allure


URL_login = 'https://stellarburgers.nomoreparties.site/api/auth/login'
URL_user = 'https://stellarburgers.nomoreparties.site/api/auth/user'

class TestUserChange:

    @allure.title('Тест: Изменение данных авторизованного пользователя')
    @pytest.mark.parametrize('value', ["email", "password", "name"])
    def test_change_authorised_user(self, register_user_and_return_its_data, generate_random_string, value):

        payload = register_user_and_return_its_data
        resp = requests.post(URL_login, data=payload)
        value = generate_random_string
        response = requests.patch(URL_user, data=value, headers={'authorization': resp.json()["accessToken"]})

        assert response.status_code == 200
        assert '"success":true' in response.text

    @allure.title('Тест: Изменение данных пользователя без авторизации')
    @pytest.mark.parametrize('value', ["email", "password", "name"])
    def test_change_non_authorised_user(self, register_user_and_return_its_data, generate_random_string, value):

        value = generate_random_string
        response = requests.patch(URL_user, data=value)

        assert response.status_code == 401
        assert response.text == '{"success":false,"message":"You should be authorised"}'
