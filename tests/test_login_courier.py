import allure
import pytest
import requests
from urls import Url

class TestLoginCourier:
    @allure.title('Авторизация курьера')
    def test_login_courier(self, creating_courier):
        with allure.step('Проверка успешной авторизации курьера: возвращает правильный код ответа - 200 и запрос возвращает id {"id": 526786}'):
            # Получаем логин и пароль из фикстуры
            login_data = {
                "login": creating_courier["login"],  # Используем тот же логин
                "password": creating_courier["password"], # Используем тот же пароль
            }

            # Авторизация курьера
            response = requests.post(Url.BASE_URL + Url.COURIER_LOGIN_URL, json=login_data)

            assert response.status_code == 200
            assert 'id' in response.json()

    @pytest.mark.parametrize("login_data, expected_status_code, expected_message", [
        ({"login": "nonexistent", "password": "wrongpassword"}, 404, "Учетная запись не найдена"),
        ({"login": "", "password": "65498"}, 400, "Недостаточно данных для входа"),
        ({"login": "test_user", "password": ""}, 400, "Недостаточно данных для входа"),
        ({"password": "65498"}, 400, "Недостаточно данных для входа"),
        ({"login": "test_user"}, 400, "Недостаточно данных для входа")
    ], ids=[
        "недействительные логин и пароль",
        "пустой логин",
        "пустой пароль",
        "отсутствует логин",
        "отсутствует пароль"
    ])
    def test_login_courier_negative(self, login_data, expected_status_code, expected_message):
        with allure.step('Проверка негативных сценариев авторизации курьера'):
            # Авторизация курьера
            response = requests.post(Url.BASE_URL + Url.COURIER_LOGIN_URL, json=login_data)

            assert response.status_code == expected_status_code
            assert response.json().get("message") == expected_message