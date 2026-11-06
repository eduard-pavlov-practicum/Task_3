import pytest
import allure
from helpers.urls import FORGOT_PASSWORD_URL, RESET_PASSWORD_URL
from pages.reset_password_page import ResetPasswordPage
from helpers.helpers import generate_random_user_data


@allure.epic("Stellar Burgers UI")
@allure.feature('Восстановление пароля')
class TestPasswordRecovery:

    @allure.title('Переход на страницу восстановления пароля по кнопке "Восстановить пароль"')
    def test_forgot_password_page_opened(self, forgot_password_page):
        with allure.step(f'Проверить, что открылась страница восстановления пароля {FORGOT_PASSWORD_URL}'):
            assert forgot_password_page.is_open()

    @allure.title('После ввода почты и клика "Восстановить" происходит переход на /reset-password')
    def test_send_email_open_reset_password_page(self, forgot_password_page, driver):

        email = generate_random_user_data()['email']

        with allure.step('Ввод почты и клик по кнопке "Восстановить"'):
            forgot_password_page.enter_email(email)
            forgot_password_page.click_recover()

        with allure.step('Проверить, что произошёл переход на страницу ввода нового пароля'):
            reset_password_page = ResetPasswordPage(driver)

            assert reset_password_page.is_open()

    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его.')
    def test_show_password_icon_makes_field_active(self, forgot_password_page, driver):
        with allure.step(f'Дождаться открытия страницы восстановления пароля {FORGOT_PASSWORD_URL}'):
            is_open = forgot_password_page.is_open()

        if not is_open:
            pytest.fail(
                f'Страница восстановления пароля не открылась. Ожидался URL: {FORGOT_PASSWORD_URL}')

        email = generate_random_user_data()['email']

        with allure.step('Ввести email и нажать "Восстановить"'):
            forgot_password_page.enter_email(email)
            forgot_password_page.click_recover()

        reset_password_page = ResetPasswordPage(driver)
        reset_password_page.is_open()

        with allure.step('Клик по кнопке показать/скрыть пароль'):
            reset_password_page.show_password()

        with allure.step('Проверить, что поле пароля стало активным'):
            assert reset_password_page.is_password_field_active()
