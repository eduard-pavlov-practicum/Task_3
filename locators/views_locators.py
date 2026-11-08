from selenium.webdriver.common.by import By


class IngredientDetailsViewLocators:

    TITLE = (By.XPATH, '//h2[text()="Детали ингредиента"]')
    INGREDIENT_NAME = (
        By.XPATH,
        '//h2[text()="Детали ингредиента"]/following-sibling::p[contains(@class, "text_type_main-medium")]',
    )
    STATS_ITEMS = (
        By.XPATH,
        '//h2[text()="Детали ингредиента"]/parent::div//li[contains(@class, "Modal_modal__statsListItem")]',
    )
    CLOSE_BUTTON = (
        By.XPATH,
        '//h2[text()="Детали ингредиента"]/ancestor::section//button[contains(@class, "Modal_modal__close")]',
    )


class OrderCreatedViewLocators:

    ORDER_ID_LABEL = (By.XPATH, '//p[text()="идентификатор заказа"]')
    ORDER_NUMBER = (
        By.XPATH,
        '//p[text()="идентификатор заказа"]/preceding-sibling::h2[contains(@class, "Modal_modal__title_shadow")]',
    )
    CLOSE_BUTTON = (
        By.XPATH,
        '//p[text()="идентификатор заказа"]/ancestor::section//button[contains(@class, "Modal_modal__close")]',
    )


class OrderDetailsViewLocators:

    ORDER_NUMBER = (By.XPATH, '//*[starts-with(normalize-space(text()), "#")]')
    CLOSE_BUTTON = (
        By.XPATH,
        '//*[starts-with(normalize-space(text()), "#")]/ancestor::section'
        '//button[contains(@class, "Modal_modal__close")]',
    )
