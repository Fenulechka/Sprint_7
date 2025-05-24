import requests
from urls import Url
from faker import Faker

fake = Faker()

class CourierAPI:
    @staticmethod
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

    @staticmethod
    def delete_courier(courier_id):
        # Удаляет курьера по ID
        requests.delete(Url.BASE_URL + Url.COURIER_DELETE_URL.format(id=courier_id))