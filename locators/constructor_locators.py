from selenium.webdriver.common.by import By


class ConstructorLocators:
    """Локаторы главной страницы /."""

    CONSTRUCTOR_BASKET_SECTION = (
        By.XPATH, '//section[contains(@class, "BurgerConstructor_basket")]')

    ORDER_BUTTON = (By.XPATH, '//button[text()="Оформить заказ"]')
    TOTAL_PRICE = (By.CSS_SELECTOR,
                   '[class*="BurgerConstructor_basket__totalContainer"] p')

    @staticmethod
    def ingredient_card(ingredient_name: str):
        return By.XPATH, f'//a[.//img[@alt="{ingredient_name}"]]'

    @staticmethod
    def ingredient_counter(ingredient_name: str):
        return (
            By.XPATH,
            f'//a[.//img[@alt="{ingredient_name}"]]//p[contains(@class, "counter_counter__num")]',
        )
