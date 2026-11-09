from selenium.webdriver.common.by import By


class IngredientDetailsViewLocators:

    TITLE = (By.XPATH, '//h2[text()="Детали ингредиента"]')
    INGREDIENT_NAME = (
        By.XPATH,
        '//h2[text()="Детали ингредиента"]/following-sibling::p[contains(@class, "text_type_main-medium")]',
    )
    CLOSE_BUTTON = (
        By.XPATH,
        '//h2[text()="Детали ингредиента"]/ancestor::section//button[contains(@class, "Modal_modal__close")]',
    )
