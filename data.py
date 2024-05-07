class DataLinks:

    URL_login = 'https://stellarburgers.nomoreparties.site/api/auth/login'
    URL_orders = 'https://stellarburgers.nomoreparties.site/api/orders'
    URL_ingredients = 'https://stellarburgers.nomoreparties.site/api/ingredients'
    URL_user = 'https://stellarburgers.nomoreparties.site/api/auth/user'
    URL_register = 'https://stellarburgers.nomoreparties.site/api/auth/register'


class DataRespTexts:

    text_200_success = '"success":true'
    text_200_token = 'accessToken'

    text_400_order = '{"success":false,"message":"Ingredient ids must be provided"}'

    text_401_incorrect = '{"success":false,"message":"email or password are incorrect"}'
    text_401_unauthorised = '{"success":false,"message":"You should be authorised"}'

    text_403_existing = '{"success":false,"message":"User already exists"}'
    text_403_missing = '{"success":false,"message":"Email, password and name are required fields"}'

    text_500 = "Internal Server Error"

