import allure
import requests
from input_data import OrderData, Data


class Order:
    post_new_order = '/api/v1/orders'
    get_order = '/api/v1/orders'

    @allure.title('Отправляем Post запрос на создаем новый заказ')
    def create_new_order(self, data):
        response = requests.post(Data.main_url+self.post_new_order, json=data)
        return response

    @allure.title('Отправляем Get запрос на получения списка заказов')
    def get_order_list(self):
        response = requests.get(Data.main_url+self.get_order)
        return response