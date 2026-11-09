from selenium.webdriver.common.by import By


class ProfileLocators:
    """Локаторы раздела /account/profile."""

    ORDER_HISTORY_NAVIGATOR_ITEM = (By.XPATH, '//a[text()="История заказов"]')
    LOGOUT_NAVIGATOR_ITEM = (By.XPATH, '//button[text()="Выход"]')
    NAME_INPUT = (By.CSS_SELECTOR, 'input[name="Name"]')
