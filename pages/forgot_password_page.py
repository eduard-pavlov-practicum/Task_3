from locators.forgot_password_locators import ForgotPasswordLocators
from pages.base_page import BasePage
from helpers.urls import FORGOT_PASSWORD_URL


class ForgotPasswordPage(BasePage):
    """Page Object страницы /forgot-password."""

    def is_open(self) -> bool:
        return self._is_open(FORGOT_PASSWORD_URL, ForgotPasswordLocators.HEADING)

    def enter_email(self, email: str):
        self.fill_input(ForgotPasswordLocators.EMAIL_INPUT, email)

    def click_recover(self):
        self.click_element(
            self.find_element_with_scroll(ForgotPasswordLocators.RECOVER_BUTTON))
