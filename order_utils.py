import requests
from urls import Url

class OrderAPI:
    @staticmethod
    def cancel_order(track):
        requests.put(Url.BASE_URL + Url.CANCEL_ORDER_URL, json={"track": track})