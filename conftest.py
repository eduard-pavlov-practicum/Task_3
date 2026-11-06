import pytest
import allure
from selenium import webdriver
from helpers.constants import BASE_URL
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage


def pytest_addoption(parser):
    """Регистрирует новый параметр командной строки --browser."""
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Браузер для тестов: chrome или firefox",
    )


@pytest.fixture(scope="function")
def driver(request):
    """Фикстура-фабрика для инициализации WebDriver."""
    browser_name = request.config.getoption("browser").lower()

    if browser_name == "chrome":
        driver = init_chrome()
    elif browser_name == "firefox":
        driver = init_firefox()
    else:
        raise pytest.UsageError(
            f"Браузер '{browser_name}' не поддерживается."
        )

    driver.maximize_window()
    driver.implicitly_wait(10)
    open_page(driver, BASE_URL)

    yield driver

    driver.quit()


@allure.step('Открываем браузер Firefox')
def init_firefox():
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=options)
    return driver


@allure.step('Открываем браузер Google Chrome')  # декоратор
def init_chrome():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    return driver


@allure.step('Открываем страницу {page}')
def open_page(driver, page):
    driver.get(page)


@allure.step('Закрываем браузер')
def quit_driver(driver):
    driver.quit()


@pytest.fixture
@allure.step('Кликнуть "Личный кабинет" на главной странице')
def login_page(driver):
    login_page = LoginPage(driver)
    login_page.open()
    return login_page


@pytest.fixture
@allure.step('Кликнуть "Восстановить пароль" на странице логина в Личный кабинет')
def forgot_password_page(login_page, driver):
    login_page.click_forgot_password_link()
    forgot_password_page = ForgotPasswordPage(driver)
    return forgot_password_page
