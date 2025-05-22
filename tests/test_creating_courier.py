import pytest
import random
import requests
import allure
from urls import Url

class TestCreatingCourier:
    @allure.title('Создание курьера')
    def test_creating_courier(self):
        with allure.step('Проверка успешного создания курьера: возвращает правильный код ответа - 201 и запрос возвращает {ok: true}'):

            payload = {
                "login": "test_user_" + str(random.randint(1, 10000)),
                "password": "65498",
                "firstName": "test user"
            }
            response = requests.post(Url.BASE_URL + Url.COURIER_CREATING_URL, data=payload)

            assert response.status_code == 201
            assert response.json() == {"ok":True}

            # Удаляем курьера после теста
            courier_id = response.json().get("id")
            if courier_id:
                requests.delete(Url.BASE_URL + Url.COURIER_DELETE_URL.format(id=courier_id))


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
            assert 'Этот логин уже используется' in response.json().get('message')


    @pytest.mark.parametrize("payload,expected_message", [
        # Нет логина
        (
                {"password": "65498", "firstName": "test user"},
                "Недостаточно данных для создания учетной записи"
        ),
        # Нет пароля
        (
                {"login": "test user", "firstName": "test user"},
                "Недостаточно данных для создания учетной записи"
        ),
        # Нет логина и пароля
        (
                {"firstName": "test user"},
                "Недостаточно данных для создания учетной записи"
        ),
        # Пустой логин
        (
                {"login": "", "password": "65498", "firstName": "test user"},
                "Недостаточно данных для создания учетной записи"
        ),
        # Пустой пароль
        (
                {"login": "test user 2", "password": "", "firstName": "test user"},
                "Недостаточно данных для создания учетной записи"
        ),
    ], ids=[
        "отсутствует логин",
        "отсутствует пароль",
        "отсутствует логин и пароль",
        "пустой логин",
        "пустой пароль"
    ])
    def test_create_courier_negative(self, payload, expected_message):
        with allure.step('Негативные проверки создания курьера'):
            response = requests.post(
                Url.BASE_URL + Url.COURIER_CREATING_URL,
                json=payload
            )

        with allure.step("Проверка ответа"):
            assert response.status_code == 400
            assert response.json()["message"] == expected_message

        with allure.step("Проверка что курьер не создался"):
            if "login" in payload and payload["login"]:
                login_response = requests.post(
                    Url.BASE_URL + Url.COURIER_LOGIN_URL,
                    json={"login": payload["login"], "password": payload.get("password", "")}
                )
                assert login_response.status_code != 200