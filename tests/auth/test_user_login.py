import requests
import allure


URL_login = 'https://stellarburgers.nomoreparties.site/api/auth/login'
URL_user = 'https://stellarburgers.nomoreparties.site/api/auth/user'


class TestUserLogin:

    @allure.title('Тест: Логин существующего пользователя')
    def test_login_existing_user(self, register_user_and_return_its_data):

        payload = register_user_and_return_its_data
        response = requests.post(URL_login, data=payload)

        assert response.status_code == 200
        assert '"success":true' in response.text

    @allure.title('Тест: Логин несуществующего пользователя')
    def test_login_non_existing_user(self, generate_and_return_login_password_without_registration):

        payload = generate_and_return_login_password_without_registration
        response = requests.post(URL_login, data=payload)

        assert response.status_code == 401
        assert response.text == '{"success":false,"message":"email or password are incorrect"}'
