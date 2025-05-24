import pytest
from courier_utils import CourierAPI
from order_utils import OrderAPI

@pytest.fixture
def creating_courier():
    # Фикстура создает курьера и возвращает его данные, затем удаляет
    login, password, courier_id = CourierAPI.create_courier()

    yield {
        'login': login,
        'password': password,
        'courier_id': courier_id
    }

    CourierAPI.delete_courier(courier_id)


@pytest.fixture
def cancel_orders():
    tracks = []
    yield tracks
    # После теста
    for track in tracks:
        OrderAPI.cancel_order(track)
