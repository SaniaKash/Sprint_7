import allure
from methods.order import Order


class TestOrderList:

    @allure.title('Проверка получения списка заказов.')
    def test_get_order_list_success(self):
        order = Order()
        response = order.get_order_list()
        assert response.status_code == 200
        assert response.json()["orders"]


