import requests

URL_login = 'https://stellarburgers.nomoreparties.site/api/auth/login'
URL_orders = 'https://stellarburgers.nomoreparties.site/api/orders'


class TestOrderReceivement:

    def test_receive_orders_authorized_user(self, register_user_and_return_its_data):

        payload = register_user_and_return_its_data
        resp = requests.post(URL_login, data=payload)
        response = requests.get(URL_orders, headers={'authorization': resp.json()["accessToken"]})

        assert response.status_code == 200
        assert '"success":true' in response.text

    def test_receive_orders_unauthorized_user(self):

        response = requests.get(URL_orders)

        assert response.status_code == 401
        assert response.text == '{"success":false,"message":"You should be authorised"}'
