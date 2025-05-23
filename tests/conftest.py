import requests
import pytest
from faker import Faker
from urls import Url

fake = Faker()

def create_courier():
    payload = {
        "login": fake.user_name(),
        "password": fake.password(),
        "firstName": fake.first_name()
    }

    # Создаем курьера
    requests.post(Url.BASE_URL + Url.COURIER_CREATING_URL, json=payload)

    # Получаем ID через ручку логина
    login_response = requests.post(
        Url.BASE_URL + Url.COURIER_LOGIN_URL,
        json={"login": payload["login"], "password": payload["password"]}
    )

    courier_id = login_response.json().get("id")

    return payload['login'], payload['password'], courier_id

def delete_courier(courier_id):
    # Удаляет курьера по ID
    requests.delete(Url.BASE_URL + Url.COURIER_DELETE_URL.format(id=courier_id))

@pytest.fixture
def creating_courier():
    # Фикстура создает курьера и возвращает его данные, затем удаляет
    login, password, courier_id = create_courier()

    yield {
        'login': login,
        'password': password,
        'courier_id': courier_id
    }

    delete_courier(courier_id)


@pytest.fixture
def cancel_orders():
    tracks = []
    yield tracks
    # После теста
    for track in tracks:
        requests.put(Url.BASE_URL + Url.CANCEL_ORDER_URL, json={"track": track})
