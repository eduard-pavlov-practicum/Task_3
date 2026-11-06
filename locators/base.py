from selenium.webdriver.common.by import By

CONSTRUCTOR_LINK = (By.XPATH, '//a[.//p[text()="Конструктор"]]')
FEED_LINK = (By.XPATH, '//a[.//p[text()="Лента Заказов"]]')
PERSONAL_ACCOUNT_LINK = (By.XPATH, '//a[.//p[text()="Личный Кабинет"]]')
SPINNER = (By.CSS_SELECTOR, '[class*="Modal_modal__loading"]')
