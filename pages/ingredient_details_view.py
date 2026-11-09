from locators.ingredient_details_locators import IngredientDetailsViewLocators
from pages.base_page import BasePage


class IngredientDetailsView(BasePage):
    """
    Page Object view деталей ингредиента /ingredient/<id>.
    """

    def __init__(self, driver, ingredient_url):
        super().__init__(driver)
        self.ingredient_url = ingredient_url

    def wait_open(self):
        self.wait_change_url(self.ingredient_url)

    def is_open(self) -> bool:
        return self._is_open(self.ingredient_url, IngredientDetailsViewLocators.TITLE)

    def get_ingredient_name(self) -> str:
        return self.find_element_with_scroll(IngredientDetailsViewLocators.INGREDIENT_NAME).text

    def close(self) -> None:
        self.click_element(self.find_element_with_scroll(
            IngredientDetailsViewLocators.CLOSE_BUTTON))
        self.wait_element_invisible(IngredientDetailsViewLocators.TITLE)
