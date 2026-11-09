from selenium.common.exceptions import NoSuchElementException, TimeoutException
from locators.order_view_locators import OrderViewLocators
from pages.base_page import BasePage


class OrderView(BasePage):
    """Page Object модалки, которая появляется сразу после успешного оформления заказа."""

    def is_open(self) -> bool:
        try:
            self.find_element_with_scroll(OrderViewLocators.ORDER_ID_LABEL)
            return True
        except TimeoutException, NoSuchElementException:
            return False

    def get_order_number(self) -> str:
        return self.find_element_with_scroll(OrderViewLocators.ORDER_NUMBER).text
