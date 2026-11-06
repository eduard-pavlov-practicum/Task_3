from selenium.webdriver.common.by import By


class ResetPasswordLocators:
    """Локаторы страницы /reset-password."""

    PASSWORD_INPUT = (
        By.XPATH, '//label[text()="Пароль"]/following-sibling::input')
    PASSWORD_EYE_ICON = (
        By.XPATH,
        '//label[text()="Пароль"]/following-sibling::div[contains(@class, "input__icon-action")]',
    )
