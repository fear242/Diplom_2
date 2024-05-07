import requests
import allure
import helper
from data import DataLinks, DataRespTexts


class TestOrderCreation:

    @allure.title('Тест: Создание заказа с валидными ингредиентами')
    def test_order_creation_with_ingredients(self):
        resp = requests.get(DataLinks.URL_ingredients)
        payload = {"ingredients": [resp.json()["data"][1]["_id"]]}
        response = requests.post(DataLinks.URL_orders, data=payload)

        assert response.status_code == 200
        assert '"success":true' in response.text
        # На том основании, что позитивный тест создания заказа прошёл без авторизации, считаю тест с авторизацией
        # избыточным. В том числе, в документации нет упоминания об ошибке при создании заказа по API без авторизации.

    @allure.title('Тест: Создание заказа с невалидными ингредиентами')
    def test_order_creation_with_wrong_hash_ingredients(self):

        payload = {"ingredients": [f"{helper.generate_random_string()}"]}
        response = requests.post(DataLinks.URL_orders, data=payload)

        assert response.status_code == 500
        assert DataRespTexts.text_500 in response.text

    @allure.title('Создание заказа без ингредиентов')
    def test_order_creation_without_ingredients(self):

        payload = {"ingredients": []}
        response = requests.post(DataLinks.URL_orders, data=payload)

        assert response.status_code == 400
        assert response.text == DataRespTexts.text_400_order
