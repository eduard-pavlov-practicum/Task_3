from selenium.common.exceptions import NoSuchElementException, TimeoutException
from locators.order_details_locators import OrderDetailsViewLocators
from pages.base_page import BasePage


class OrderDetailsView(BasePage):
    """
    Page Object view с деталями заказа.
    """

    def is_open(self) -> bool:
        try:
            self.find_element_with_scroll(
                OrderDetailsViewLocators.ORDER_NUMBER)
            return True
        except TimeoutException, NoSuchElementException:
            return False

    def get_order_number(self) -> str:
        return self.find_element_with_scroll(OrderDetailsViewLocators.ORDER_NUMBER).text
