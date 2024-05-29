import requests
from input_data import OrderData


class Order:

    def create_new_order(self, data):
        response = requests.post(OrderData.url_create_order, json=data)
        return response

    def get_order_list(self):
        response = requests.get(OrderData.url_get_order_list)
        return response