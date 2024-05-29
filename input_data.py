from helpers import login, password
from faker import Faker


fake = Faker()
class Data:

    url_create_courier = 'https://qa-scooter.praktikum-services.ru/api/v1/courier'
    url_login_courier = 'https://qa-scooter.praktikum-services.ru/api/v1/courier/login'
    url_delete_courier = 'https://qa-scooter.praktikum-services.ru/api/v1/courier/'
    courier_login_password = {
            "login": f'{login()}',
            "password": f'{password()}',
            "firstName": "firstName"
            }
    courier_same_login_password_1 = {
            "login": 'aaaaaasssssaaaa',
            "password": '123456',
            "firstName": "secondName"
            }
    courier_same_login_password_2 = {
            "login": 'aaaaaasssssaaaa',
            "password": '654321',
            "firstName": "secondName"
            }
    courier_without_login = {
            "password": f'{password()}'
            }

    courier_without_password = {
            "login": f'{login()}',
            "password": ''
            }

    courier_false_login = {
            "login": f'{login()}abc',
            "password": f'{password()}',
            "firstName": "firstName"
            }
    courier_false_password = {
            "login": f'{login()}',
            "password": f'{password()}123',
            "firstName": "firstName"
            }
    courier_without_login_password = {}

class OrderData:
    url_create_order = 'https://qa-scooter.praktikum-services.ru/api/v1/orders'
    url_get_order_list = 'https://qa-scooter.praktikum-services.ru/api/v1/orders'
    order_black = {
        "firstName": "Narutasadddasdasdo",
        "lastName": "Uchasdaaasdasdfffiha",
        "address": "Konoha, 142123123 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 41 35",
        "rentTime": 5,
        "deliveryDate": "2024-06-06",
        "comment": "Saske, co Konoha",
        "color": ["BLACK"]
        }
    order_grey = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": ["GREY"]
        }
    order_black_grey = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": ["GREY","BLACK"]
    }
    order_without_color = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        }
