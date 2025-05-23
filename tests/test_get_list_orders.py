import allure
import requests
from urls import Url


class TestGetListOrders:
    @allure.title('Получение списка заказов')

    def test_get_list_orders(self):
        response = requests.get(Url.BASE_URL + Url.RETRIEVING_ORDER_LIST)

        assert response.status_code == 200

        response_data = response.json()
        assert "orders" in response_data

        # Проверяем, что "orders" - это список
        assert isinstance(response_data["orders"], list)
