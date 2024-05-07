import requests
import allure
import helper
from data import DataLinks, DataRespTexts


class TestUserLogin:

    @allure.title('Тест: Логин существующего пользователя')
    def test_login_existing_user(self, register_user_and_return_its_data):

        payload = register_user_and_return_its_data
        response = requests.post(DataLinks.URL_login, data=payload)

        assert response.status_code == 200
        assert DataRespTexts.text_200_success in response.text

    @allure.title('Тест: Логин несуществующего пользователя')
    def test_login_non_existing_user(self):

        payload = helper.generate_and_return_login_password_without_registration()
        response = requests.post(DataLinks.URL_login, data=payload)

        assert response.status_code == 401
        assert response.text == DataRespTexts.text_401_incorrect
