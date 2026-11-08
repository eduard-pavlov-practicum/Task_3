from selenium.webdriver.remote.webelement import WebElement
from helpers.urls import RESET_PASSWORD_URL
from locators.reset_password_locators import ResetPasswordLocators
from pages.base_page import BasePage


class ResetPasswordPage(BasePage):
    """Page Object страницы /reset-password."""

    def show_password(self) -> None:
        self.click_element(self.find_element_with_scroll(
            ResetPasswordLocators.PASSWORD_EYE_ICON))

    def is_password_field_active(self) -> bool:
        return self.find_element_with_scroll(ResetPasswordLocators.PASSWORD_INPUT) == self.driver.switch_to.active_element

    def is_open(self):
        return self._is_open(RESET_PASSWORD_URL, ResetPasswordLocators.PASSWORD_INPUT)
