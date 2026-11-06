from selenium.common.exceptions import TimeoutException
from helpers.urls import CONSTRUCTOR_URL
from helpers.drag_and_drop import drag_and_drop
from locators.constructor_locators import ConstructorLocators
from pages.base_page import BasePage


class ConstructorPage(BasePage):
    """Page Object страницы /reset-password."""

    def wait_open(self):
        self.wait_change_url(CONSTRUCTOR_URL)
