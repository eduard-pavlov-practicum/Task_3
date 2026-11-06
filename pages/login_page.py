from helpers.urls import LOGIN_URL
from locators.login_locators import LoginLocators
from locators.base import PERSONAL_ACCOUNT_LINK
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Page Object страницы /login."""

    def open(self):
        self.click_element(
            self.find_element_with_scroll(PERSONAL_ACCOUNT_LINK))

    def is_open(self):
        return self._is_open(LOGIN_URL, LoginLocators.EMAIL_INPUT)

    def login(self, email: str, password: str):
        self.fill_input(LoginLocators.EMAIL_INPUT, email)
        self.fill_input(LoginLocators.PASSWORD_INPUT, password)
        self.click_element(self.find_element_with_scroll(
            LoginLocators.LOGIN_BUTTON))

    def click_forgot_password_link(self):
        self.click_element(
            self.find_element_with_scroll(LoginLocators.FORGOT_PASSWORD_LINK))
