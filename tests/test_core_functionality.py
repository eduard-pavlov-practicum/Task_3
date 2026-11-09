import allure

from pages.feed_page import FeedPage
from pages.constructor_page import ConstructorPage


@allure.epic("Stellar Burgers UI")
@allure.feature('Основной функционал')
class TestCoreFunctionality:

    @allure.title('Переход в конструктор по клику на "Конструктор"')
    def test_navigate_to_constructor(self, login_page):
        login_page.navigate_to_constructor()
        constructor_page = ConstructorPage(login_page.driver)
        constructor_page.wait_open()

        with allure.step('Проверить, что открылась страница конструктора'):
            assert constructor_page.is_open()

    @allure.title('Переход в ленту заказов по клику на "Лента заказов"')
    def test_navigate_to_feed(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.navigate_to_feed()
        feed_page = FeedPage(constructor_page.driver)

        with allure.step('Проверить, что открылась лента заказов'):
            assert feed_page.is_open()

    @allure.title('Если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_click_by_ingredient_opens_detail_view(self, driver, ingredients):
        constructor_page = ConstructorPage(driver)
        ingredient_name = ingredients['sauce'][0]['name']

        with allure.step(f'Кликнуть на ингредиент "{ingredient_name}"'):
            ingredient_view = constructor_page.open_ingredient_details(
                ingredient_name)

        with allure.step('Проверить, что всплывающее окно с деталями именно этого ингредиента'):
            assert ingredient_view.is_open()
            assert ingredient_view.get_ingredient_name() == ingredient_name

    @allure.title('Всплывающее окно с деталями ингредиента закрывается по крестику')
    def test_close_ingredient_view_by_cross_icon(self, driver, ingredients):
        constructor_page = ConstructorPage(driver)
        ingredient_name = ingredients['sauce'][0]['name']
        ingredient_view = constructor_page.open_ingredient_details(
            ingredient_name)
        with allure.step('Закрыть всплывающее окно по крестику'):
            ingredient_view.close()

        with allure.step('Проверить, что всплывающее окно закрылось'):
            assert not ingredient_view.is_open()

    @allure.title('При добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    def test_add_ingredient_increases_counter(self, constructor_page, ingredients):
        ingredient_name = ingredients['main'][0]['name']

        with allure.step('Проверить, что количество ингредиента равно 0'):
            assert constructor_page.get_ingredient_counter(
                ingredient_name) == 0

        with allure.step(f'Перетащить ингредиент "{ingredient_name}" в конструктор'):
            constructor_page.add_ingredient_to_constructor(ingredient_name)

        with allure.step('Проверить, что каунтер ингредиента увеличился до 1'):
            assert constructor_page.get_ingredient_counter(
                ingredient_name) == 1

    @allure.title('Залогиненный пользователь может оформить заказ')
    def test_logged_in_user_can_create_order(self, constructor_page, ingredients):
        bun_name = ingredients['bun'][0]['name']
        ingredient_name = ingredients['main'][0]['name']

        with allure.step('Собираем бургер из первой попавшейся булки и начинки'):
            constructor_page.add_ingredient_to_constructor(bun_name)
            constructor_page.add_ingredient_to_constructor(ingredient_name)

        with allure.step('Нажимаем "Оформить заказ"'):
            order_modal = constructor_page.click_order_button()

        with allure.step('Проверяем, что заказ оформлен и показан его номер'):
            assert order_modal.is_open()
            assert order_modal.get_order_number().isdigit()
