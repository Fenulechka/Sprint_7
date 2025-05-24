testdata = [
    {
        "firstName": "Иван",
        "lastName": "Кличко",
        "address": "ул. Ленина, 1",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 3,
        "deliveryDate": "2025-06-06",
        "comment": "Позвонить за час",
        "color": ["BLACK"]
    },
    {
        "firstName": "Иван",
        "lastName": "Кличко",
        "address": "ул. Ленина, 1",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 3,
        "deliveryDate": "2025-06-06",
        "comment": "Позвонить за час",
        "color": ["GREY"]
    },
    {
        "firstName": "Иван",
        "lastName": "Кличко",
        "address": "ул. Ленина, 1",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 3,
        "deliveryDate": "2025-06-06",
        "comment": "Позвонить за час",
        "color": ["BLACK", "GREY"]
    },
    {
        "firstName": "Иван",
        "lastName": "Кличко",
        "address": "ул. Ленина, 1",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 3,
        "deliveryDate": "2025-06-06",
        "comment": "Позвонить за час",
        "color": []  # пустой массив цветов
    }
]


negative_cases = [
    # Отсутствует логин
    ({
        "password": "65498",
        "firstName": "test user"
    }, "Недостаточно данных для создания учетной записи"),

    # Отсутствует пароль
    ({
        "login": "test user",
        "firstName": "test user"
    }, "Недостаточно данных для создания учетной записи"),

    # Отсутствуют логин и пароль
    ({
        "firstName": "test user"
    }, "Недостаточно данных для создания учетной записи"),

    # Пустой логин
    ({
        "login": "",
        "password": "65498",
        "firstName": "test user"
    }, "Недостаточно данных для создания учетной записи"),

    # Пустой пароль
    ({
        "login": "test user 2",
        "password": "",
        "firstName": "test user"
    }, "Недостаточно данных для создания учетной записи")
]


negative_cases_test_names = [
    "missing_login",           # отсутствует логин
    "missing_password",        # отсутствует пароль
    "missing_both_fields",     # отсутствует логин и пароль
    "empty_login",             # пустой логин
    "empty_password"           # пустой пароль
]


server_messages = {
    "duplicate_login": "Этот логин уже используется"
    # Другие возможные сообщения...
}


negative_login_data = [
    ({"login": "nonexistent", "password": "wrongpassword"}, 404, "Учетная запись не найдена"),
    ({"login": "", "password": "65498"}, 400, "Недостаточно данных для входа"),
    ({"login": "test_user", "password": ""}, 400, "Недостаточно данных для входа"),
    ({"password": "65498"}, 400, "Недостаточно данных для входа"),
    ({"login": "test_user"}, 400, "Недостаточно данных для входа")
]

negative_login_test_names = [
    "invalid_credentials",  # недействительные логин и пароль
    "empty_login",         # пустой логин
    "empty_password",      # пустой пароль
    "missing_login",       # отсутствует логин
    "missing_password"     # отсутствует пароль
]