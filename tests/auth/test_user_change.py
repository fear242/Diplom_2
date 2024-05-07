import pytest
import requests
import allure
import helper
from data import DataLinks, DataRespTexts


class TestUserChange:

    @allure.title('Тест: Изменение данных авторизованного пользователя')
    @pytest.mark.parametrize('value', ["email", "password", "name"])
    def test_change_authorised_user(self, register_user_and_return_its_data, value):

        payload = register_user_and_return_its_data
        resp = requests.post(DataLinks.URL_login, data=payload)
        data = '{'f'{value}={helper.generate_random_string()}''}'
        response = requests.patch(DataLinks.URL_user, data=data, headers={'authorization': resp.json()["accessToken"]})

        assert response.status_code == 200
        assert DataRespTexts.text_200_success in response.text

    @allure.title('Тест: Изменение данных пользователя без авторизации')
    @pytest.mark.parametrize('value', ["email", "password", "name"])
    def test_change_non_authorised_user(self, register_user_and_return_its_data, value):

        value = helper.generate_random_string()
        response = requests.patch(DataLinks.URL_user, data=value)

        assert response.status_code == 401
        assert response.text == DataRespTexts.text_401_unauthorised
