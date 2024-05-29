import allure
import pytest
from input_data import Data
from methods.courier import Courier


class TestCreateCourier:

    @allure.title('Проверка успешного создания курьера при заполнении всех полей. Успешное создание на запрос '
                  'возвращает {"ok":true} ')
    def test_post_create_courier_success(self):
        courier = Courier()
        response = courier.create_new_courier(Data.courier_login_password)
        assert response.status_code == 200
        assert response.text == '{"ok":true}'

    @allure.title('Проверка возвращении ошибки при создание одинаковых курьеров ')
    def test_post_create_2_same_courier_failed(self):
        courier = Courier()
        create_courier_1 = courier.create_new_courier(Data.courier_login_password)
        create_courier_2 = courier.create_new_courier(Data.courier_login_password)
        assert create_courier_2.status_code == 409

    @allure.title('Проверка возвращении ошибки при создании курьера с одинаковым логином')
    def test_post_create_2_same_login_courier_failed(self):
        courier = Courier()
        courier.create_new_courier(Data.courier_same_login_password_1)
        create_courier_same_login = courier.create_new_courier(Data.courier_same_login_password_2)
        assert create_courier_same_login.status_code == 409

    @allure.title('Проверка возвращении ошибки при отсутствии поля логина или пароля при создании курьера')
    @pytest.mark.parametrize('data', (Data.courier_without_login, Data.courier_without_password, Data.courier_without_login_password))
    def test_post_create_courier_without_password_or_login_failed(self, data):
        courier = Courier()
        response = courier.create_new_courier(data)
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"

