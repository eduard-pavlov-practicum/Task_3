from helpers.urls import CONSTRUCTOR_URL, PROFILE_URL
from locators.profile_locators import ProfileLocators
from pages.base_page import BasePage
from pages.orders_history_page import OrdersHistoryPage


class ProfilePage(BasePage):
    """Page Object раздела /account/profile."""

    def wait_open(self) -> 'ProfilePage':
        self.wait_change_url(PROFILE_URL)
        return self

    def is_open(self) -> bool:
        return self._is_open(PROFILE_URL, ProfileLocators.NAME_INPUT)

    def navigate_to_orders_history(self) -> OrdersHistoryPage:
        self.click_element(self.find_element_with_scroll(
            ProfileLocators.ORDER_HISTORY_NAVIGATOR_ITEM))
        return OrdersHistoryPage(self.driver)

    def logout(self):
        self.click_element(self.find_element_with_scroll(
            ProfileLocators.LOGOUT_NAVIGATOR_ITEM))
