import allure
import pytest
from input_data import Data
from methods.courier import Courier


class TestLoginCourier:

    @allure.title('Проверка успешной авторизации курьера при заполнении всех полей. Успешная авторизация на запрос '
                  'возвращает id курьера')
    def test_post_login_courier_return_id_success(self):
        courier = Courier()
        courier.create_new_courier(Data.courier_login_password)
        response = courier.login_courier(Data.courier_login_password)
        assert response.status_code == 200
        assert response.json()['id']

    @allure.title('Проверка возвращении ошибки при авторизации несуществующего пользователем')
    def test_post_login_courier_wrong_login_or_password_failed(self):
        courier = Courier()
        response = courier.login_courier(Data.courier_login_password)
        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"


    @allure.title('Проверка возвращении ошибки на неверный логин или пароль при авторизации')
    @pytest.mark.parametrize('data', (Data.courier_false_login, Data.courier_false_password))
    def test_post_login_courier_wrong_login_or_password_failed(self, data):
        courier = Courier()
        courier.create_new_courier(Data.courier_login_password)
        response = courier.login_courier(data)
        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"



    @allure.title('Проверка возвращении ошибки при отсутствии поля логина или пароля при авторизации')
    @pytest.mark.parametrize('data', (Data.courier_without_login, Data.courier_without_password))
    def test_post_login_courier_without_login_or_password_field_failed(self, data):
        courier = Courier()
        courier.create_new_courier(Data.courier_login_password)
        response = courier.login_courier(data)
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"