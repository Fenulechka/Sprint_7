import pytest
import random
import requests
import allure
from urls import Url
from data import negative_cases, negative_cases_test_names, server_messages

class TestCreatingCourier:
    @allure.title('Создание курьера')
    def test_creating_courier(self, creating_courier):
        with allure.step('Проверка успешного создания курьера: возвращает правильный код ответа - 201 и запрос возвращает {ok: true}'):

            payload = {
                "login": creating_courier['login']+ str(random.randint(1, 10000)),
                "password": creating_courier['password'],
                "firstName": "test user"
            }
            response = requests.post(Url.BASE_URL + Url.COURIER_CREATING_URL, data=payload)

            assert response.status_code == 201
            assert response.json() == {"ok":True}


    def test_creating_courier_duplicate_login(self, creating_courier):
        with allure.step('Тест проверяет, что нельзя создать курьера с уже существующим логином'):
            # Получаем логин и пароль из фикстуры
            duplicate_data = {
                "login": creating_courier["login"],  # Используем тот же логин
                "password": "any_password",
                "firstName": "any_name"
            }

            # Попытка зарегистрировать курьера с тем же логином
            response = requests.post(Url.BASE_URL + Url.COURIER_CREATING_URL, json=duplicate_data)

            assert response.status_code == 409
            assert server_messages["duplicate_login"] in response.json().get('message')


    @pytest.mark.parametrize("payload,expected_message", negative_cases, ids=negative_cases_test_names)
    def test_create_courier_negative(self, payload, expected_message):
        with allure.step('Негативные проверки создания курьера'):
            response = requests.post(
                Url.BASE_URL + Url.COURIER_CREATING_URL,
                json=payload
            )

        with allure.step("Проверка ответа"):
            assert response.status_code == 400
            assert response.json()["message"] == expected_message
