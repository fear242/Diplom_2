import requests
import allure
from data import DataLinks, DataRespTexts


class TestOrderReceivement:

    @allure.title('Тест: Получение списка заказов авторизованного пользователя')
    def test_receive_orders_authorized_user(self, register_user_and_return_its_data):

        payload = register_user_and_return_its_data
        resp = requests.post(DataLinks.URL_login, data=payload)
        response = requests.get(DataLinks.URL_orders, headers={'authorization': resp.json()["accessToken"]})

        assert response.status_code == 200
        assert DataRespTexts.text_200_success in response.text

    @allure.title('Тест: Получение списка заказов неавторизованного пользователя')
    def test_receive_orders_unauthorized_user(self):

        response = requests.get(DataLinks.URL_orders)

        assert response.status_code == 401
        assert response.text == DataRespTexts.text_401_unauthorised
