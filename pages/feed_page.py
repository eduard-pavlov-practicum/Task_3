from selenium.common.exceptions import TimeoutException

from helpers.urls import FEED_URL
from locators.feed_locators import FeedLocators
from pages.base_page import BasePage, UPDATE_TIMEOUT
from pages.order_details_view import OrderDetailsView


class FeedPage(BasePage):
    """Page Object страницы /feed."""

    def wait_open(self) -> 'FeedPage':
        self.wait_change_url(FEED_URL)
        return self

    def is_open(self) -> bool:
        self.wait_open()
        return self._is_open(FEED_URL, FeedLocators.ORDER_CARDS)

    def get_order_numbers(self) -> list[str]:
        return [element.text for element in self.find_elements(FeedLocators.ORDER_CARD_NUMBERS)]

    def open_first_order(self) -> OrderDetailsView:
        self.click_element(self.find_element_with_scroll(
            FeedLocators.ORDER_CARDS))
        return OrderDetailsView(self.driver)

    def get_total_done_count(self) -> int:
        return int(self.find_element_with_scroll(FeedLocators.TOTAL_DONE_COUNT).text)

    def get_today_done_count(self) -> int:
        return int(self.find_element_with_scroll(FeedLocators.TODAY_DONE_COUNT).text)

    def get_in_progress_order_numbers(self) -> list[str]:
        return [element.text.strip() for element in self.find_elements(FeedLocators.IN_PROGRESS_ORDERS_LIST)]

    def wait_for_order_in_progress(self, order_number: str) -> bool:
        """
        Дожидаемся появления заказа order_number в списке "В работе".
        Лента обновляется асинхронно, поэтому достаточно опрашивать список заказов.
        """

        last_viewed_order_numbers: list[str] = []

        def _order_is_present(_driver) -> bool:
            nonlocal last_viewed_order_numbers
            last_viewed_order_numbers = self.get_in_progress_order_numbers()
            if order_number in last_viewed_order_numbers:
                return True
            return False

        try:
            self.wait_until(_order_is_present)
            return True
        except TimeoutException as exc:
            raise TimeoutError(
                f'Заказ {order_number} не появился в разделе "В работе" за {UPDATE_TIMEOUT} секунд. Последний список: {last_viewed_order_numbers}'
            ) from exc
