import requests
from input_data import Data
import json


class Courier:

    def create_new_courier(self, data):
        response = requests.post(Data.url_create_courier, json=data)
        return response

    def login_courier(self, data_login_password):
        response = requests.post(Data.url_login_courier, json=data_login_password)
        return response




