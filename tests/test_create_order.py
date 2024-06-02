import allure
import pytest
from input_data import OrderData
from methods.order import Order


class TestOrder:

    @allure.title('Проверка создания заказа при указании цветов : Серый , черный , серый и черный, без указания '
                  'цвета. Тело ответа содержит "track"')
    @pytest.mark.parametrize('data', (
    OrderData.order_black, OrderData.order_grey, OrderData.order_black_grey, OrderData.order_without_color))
    def test_post_create_order_colors_without_colors_success(self, data):
        order = Order()
        response = order.create_new_order(data)
        assert response.status_code == 201
        assert response.json()["track"]
