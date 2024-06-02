from helpers import login, password
from faker import Faker


fake = Faker()
class Data:

    main_url = 'https://qa-scooter.praktikum-services.ru'
    create_courier_success_message = '{"ok":true}'
    create_courier_same_login_message = "Этот логин уже используется"
    create_courier_without_login_or_password = "Недостаточно данных для создания учетной записи"
    login_courier_no_exist_message = "Учетная запись не найдена"
    login_courier_wrong_login_or_password_message = "Учетная запись не найдена"
    login_courier_without_login_or_password_field_message = "Недостаточно данных для входа"
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
    courier_not_exist = {
            "login": f'{login()}',
            "password": f'{password()}123'
            }
    courier_without_login_password = {}


class OrderData:

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
