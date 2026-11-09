from selenium.webdriver.common.by import By


class OrdersHistoryLocators:
    """Локаторы раздела /account/order-history."""

    ORDER_NUMBERS = (
        By.CSS_SELECTOR,
        '[class*="OrderHistory_orderHistory"] p[class*="text_type_digits-default"]',
    )
