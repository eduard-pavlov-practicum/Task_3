import allure
from pages.login_page import LoginPage


@allure.epic("Stellar Burgers UI")
@allure.feature('Личный кабинет')
class TestPersonalAccount:
    """Тесты раздела /account (доступен только авторизованному пользователю)."""

    @allure.title('Переход в личный кабинет по клику на "Личный Кабинет" в шапке')
    def test_navigate_to_personal_account(self, profile_page):
        with allure.step('Проверить, что открылся личный кабинет'):
            assert profile_page.is_open()

    @allure.title('Переход в раздел "История заказов"')
    def test_navigate_to_order_history(self, profile_page):
        with allure.step('Кликнуть кнопку "История заказов"'):
            order_history = profile_page.navigate_to_orders_history()
            order_history.wait_open()

        with allure.step('Проверить, что открылась история заказов'):
            assert order_history.is_open()

    @allure.title('Выход из аккаунта.')
    def test_logout(self, profile_page):

        with allure.step('Кликнуть кнопку "Выход"'):
            profile_page.logout()

        with allure.step('Убедиться, что пользователь действительно вышел и открыта страница /login'):
            login_page = LoginPage(profile_page.driver)
            assert login_page.is_open()
