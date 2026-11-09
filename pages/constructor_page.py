from selenium.common.exceptions import TimeoutException
from helpers.urls import CONSTRUCTOR_URL
from helpers.drag_and_drop import drag_and_drop
from locators.constructor_locators import ConstructorLocators
from pages.base_page import BasePage
from pages.ingredient_details_view import IngredientDetailsView
from pages.order_view import OrderView


class ConstructorPage(BasePage):
    """Page Object страницы /reset-password."""

    def wait_open(self):
        self.wait_change_url(CONSTRUCTOR_URL)

    def is_open(self) -> bool:
        return self._is_open(CONSTRUCTOR_URL)

    def open_ingredient_details(self, ingredient_name: str) -> IngredientDetailsView:
        ingredient_element = self.find_element_with_scroll(
            ConstructorLocators.ingredient_card(ingredient_name))
        ingredient_url = ingredient_element.get_attribute("href")
        self.click_element(self.find_element_with_scroll(
            ConstructorLocators.ingredient_card(ingredient_name)))
        ingredient_view = IngredientDetailsView(self.driver, ingredient_url)
        ingredient_view.wait_open
        return ingredient_view

    def add_ingredient_to_constructor(self, ingredient_name: str) -> None:
        source = self.find_element_with_scroll(
            ConstructorLocators.ingredient_card(ingredient_name))
        target = self.find_element_with_scroll(
            ConstructorLocators.CONSTRUCTOR_BASKET_SECTION)
        drag_and_drop(self.driver, source, target)

    def get_ingredient_counter(self, ingredient_name: str) -> int:
        try:
            counter_text = self.find_element_with_scroll(
                ConstructorLocators.ingredient_counter(ingredient_name)).text
        except TimeoutException:
            return 0
        return int(counter_text)

    def click_order_button(self) -> OrderView:
        self.click_element(self.find_element_with_scroll(
            ConstructorLocators.ORDER_BUTTON))
        return OrderView(self.driver)
