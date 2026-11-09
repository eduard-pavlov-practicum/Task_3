import allure

from pages.feed_page import FeedPage
from pages.constructor_page import ConstructorPage
from helpers.helpers import create_order, order_number_str


@allure.epic("Stellar Burgers UI")
@allure.feature('Лента заказов')
class TestOrderFeed:
    """Тесты страницы /feed."""

    @allure.title('Клик по заказу в ленте открывает view с деталями этого заказа')
    def test_click_order_opens_details_modal(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.navigate_to_feed()
        feed_page = FeedPage(constructor_page.driver)
        feed_page.wait_open()

        with allure.step('Открыть первый заказ в ленте'):
            order_modal = feed_page.open_first_order()

        with allure.step('Проверить, что появилось view с деталями заказа '):
            assert order_modal.is_open()

    @allure.title('Заказ из истории заказов пользователя отображается в ленте заказов')
    def test_user_order_appears_in_feed(self, created_order, profile_page):

        with allure.step('Открыть историю заказов и получить номер заказа пользователя'):
            order_history_page = profile_page.navigate_to_orders_history()
            order_history_page.wait_open()
            # Фикстура profile_page гарантирует нового пользователя, created_order гарантирует, что заказ единственный.
            # Мы берем номер заказа прямо со страницы истории (как это звучит в задании):
            history_orders = order_history_page.get_order_numbers()
            order_from_history = history_orders[0]
        
        with allure.step('Перейти на страницу «Лента заказов»'):
            order_history_page.navigate_to_feed()
            feed_page = FeedPage(order_history_page.driver)
            feed_page.wait_open()

        with allure.step('Проверить, что тот же заказ отображается в общей ленте заказов'):

            assert order_from_history in feed_page.get_order_numbers()

    @allure.title('При создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_total_done_orders_counter_increase_after_new_order(self, feed_page, registered_user, ingredients):

        with allure.step('Запомнить текущие значения счётчиков'):
            total_initial_count = feed_page.get_total_done_count()

        access_token = registered_user['accessToken']
        bun_id = ingredients['bun'][0]['_id']
        filling_id = ingredients['main'][0]['_id']

        with allure.step('Создать новый заказ через API'):
            create_order(
                [bun_id, filling_id], access_token).json()

        with allure.step('Проверить, что счётчик "Выполнено за сегодня" увеличился'):
            assert feed_page.get_total_done_count() > total_initial_count

    @allure.title('При создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_today_done_orders_counter_increase_after_new_order(self, feed_page, registered_user, ingredients):

        with allure.step('Запомнить текущие значения счётчиков'):
            today_initial_count = feed_page.get_today_done_count()

        access_token = registered_user['accessToken']
        bun_id = ingredients['bun'][0]['_id']
        filling_id = ingredients['main'][0]['_id']

        with allure.step('Создать новый заказ через API'):
            create_order(
                [bun_id, filling_id], access_token).json()

        with allure.step('Проверить, что счётчик "Выполнено за сегодня" увеличился'):
            assert feed_page.get_today_done_count() > today_initial_count

    @allure.title('После оформления заказа его номер появляется в разделе В работе')
    def test_new_order_appears_in_progress_section(self, feed_page, created_order):
        order_number = created_order
        formatted_number = f'{order_number:06d}'

        with allure.step('Дождаться, пока заказ появится в разделе "В работе"'):
            in_progress_orders = feed_page.wait_for_order_in_progress(
                formatted_number)
            assert in_progress_orders
