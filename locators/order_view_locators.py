from selenium.webdriver.common.by import By


class OrderViewLocators:
    """Локаторы view успешного оформления заказа."""

    ORDER_ID_LABEL = (By.XPATH, '//p[text()="идентификатор заказа"]')
    ORDER_NUMBER = (
        By.XPATH,
        '//p[text()="идентификатор заказа"]/preceding-sibling::h2[contains(@class, "Modal_modal__title_shadow")]',
    )
    CLOSE_BUTTON = (
        By.XPATH,
        '//p[text()="идентификатор заказа"]/ancestor::section//button[contains(@class, "Modal_modal__close")]',
    )
