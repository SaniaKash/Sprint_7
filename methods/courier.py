import allure
import requests
from input_data import Data
import json


class Courier:
    post_new_courier = '/api/v1/courier'
    post_login_courier = '/api/v1/courier/login'

    @allure.title('Отправляем Post запрос на создание курьера')
    def create_new_courier(self, data):
        response = requests.post(Data.main_url+self.post_new_courier, json=data)
        return response

    @allure.title('Отправляем Post запрос на авторизацию  курьера')
    def login_courier(self, data_login_password):
        response = requests.post(Data.main_url+self.post_login_courier, json=data_login_password)
        return response




