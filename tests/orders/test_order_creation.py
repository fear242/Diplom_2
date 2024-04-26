import requests


URL_orders = 'https://stellarburgers.nomoreparties.site/api/orders'
URL_ingredients = 'https://stellarburgers.nomoreparties.site/api/ingredients'


class TestOrderCreation:

    def test_order_creation_with_ingredients(self):

        resp = requests.get(URL_ingredients)
        payload = {"ingredients": [resp.json()["data"][1]["_id"]]}
        response = requests.post(URL_orders, data=payload)

        assert response.status_code == 200
        assert '"success":true' in response.text
        # На том основании, что позитивный тест создания заказа прошёл без авторизации, считаю тест с авторизацией
        # избыточным. В том числе, в документации нет упоминания об ошибке при создании заказа по API без авторизации.

    def test_order_creation_with_wrong_hash_ingredients(self, generate_random_string):

        payload = {"ingredients": [f"{generate_random_string}"]}
        response = requests.post(URL_orders, data=payload)

        assert response.status_code == 500
        assert "Internal Server Error" in response.text

    def test_order_creation_without_ingredients(self):

        payload = {"ingredients": []}
        response = requests.post(URL_orders, data=payload)

        assert response.status_code == 400
        assert response.text == '{"success":false,"message":"Ingredient ids must be provided"}'
