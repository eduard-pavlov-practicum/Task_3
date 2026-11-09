from selenium.webdriver.common.by import By


class OrderDetailsViewLocators:
    """
    Локаторы view с деталями конкретного заказа
    """

    ORDER_NUMBER = (
        By.XPATH, '//div[starts-with(@class, "Modal_orderBox")]/p[contains(@class, "text_type_digits") and starts-with(normalize-space(text()), "#")]')
    CLOSE_BUTTON = (
        By.XPATH,
        '//*[starts-with(normalize-space(text()), "#")]/ancestor::section//button[contains(@class, "Modal_modal__close")]',
    )
