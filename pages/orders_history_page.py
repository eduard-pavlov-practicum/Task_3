from typing import List

from helpers.urls import ORDER_HISTORY_URL
from locators.orders_history_locators import OrdersHistoryLocators
from pages.base_page import BasePage


class OrdersHistoryPage(BasePage):
    """Page Object раздела /account/order-history."""

    def wait_open(self) -> 'OrdersHistoryPage':
        self.wait_change_url(ORDER_HISTORY_URL)
        return self

    def is_open(self):
        return self._is_open(ORDER_HISTORY_URL)

    def find_orders(self):
        return self.driver.find_elements(*OrdersHistoryLocators.ORDER_NUMBERS)

    def get_order_numbers(self) -> List[str]:
        orders = self.find_orders()
        return [order.text for order in orders]
