class Url:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru'
    COURIER_CREATING_URL = '/api/v1/courier'
    COURIER_LOGIN_URL = '/api/v1/courier/login'
    ORDER_CREATION_URL = '/api/v1/orders'
    RETRIEVING_ORDER_LIST = '/api/v1/orders'  #без courierId
    COURIER_DELETE_URL = '/api/v1/courier/:id'
    CANCEL_ORDER_URL = '/api/v1/orders/cancel'