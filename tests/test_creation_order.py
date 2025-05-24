import allure
import pytest
import requests
from urls import Url
from data import testdata

class TestCreationOrder:
    @allure.title('Создание заказа')

    @pytest.mark.parametrize("order_data", testdata, ids=[
        "scooter_color_black",            # цвет самоката: черный
        "scooter_color_grey",             # цвет самоката: серый
        "scooter_color_black_and_grey",   # цвет самоката: черный и серый
        "color missing"                   # отсутствует цвет
    ])

    def test_creation_order(self, order_data, cancel_orders):
        with allure.step('Успешное создание заказа с разными вариантами цветов самоката, в теле ответа содержится track'):

            response = requests.post(Url.BASE_URL + Url.ORDER_CREATION_URL, json=order_data)

            assert response.status_code == 201
            assert "track" in response.json()
