import pytest
import requests
import allure
import helper
from data import DataLinks, DataRespTexts


class TestUserCreation:

    @allure.title('Тест: Регистрация нового пользователя')
    def test_register_new_user(self):

        payload = helper.generate_and_return_login_password_without_registration()
        response = requests.post(DataLinks.URL_register, data=payload)

        assert response.status_code == 200
        assert DataRespTexts.text_200_token in response.text
        requests.delete(DataLinks.URL_user, headers={'authorization': response.json()["accessToken"]})

    @allure.title('Тест: Регистрация уже зарегистрированного пользователя')
    def test_register_similar_user(self, register_user_and_return_its_data):

        payload = register_user_and_return_its_data
        response = requests.post(DataLinks.URL_register, data=payload)

        assert response.status_code == 403
        assert response.text == DataRespTexts.text_403_existing

    @allure.title('Тест: Регистрация пользователя с недостающими данными')
    @pytest.mark.parametrize('value', ["email", "password", "name"])
    def test_register_user_with_missing_data(self, value):

        payload = helper.generate_and_return_login_password_without_registration()
        payload[value] = ""
        response = requests.post(DataLinks.URL_register, data=payload)

        assert response.status_code == 403
        assert response.text == DataRespTexts.text_403_missing
