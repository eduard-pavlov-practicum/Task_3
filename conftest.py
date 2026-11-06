import pytest
import allure
from selenium import webdriver
from helpers.urls import BASE_URL
from helpers.helpers import generate_random_user_data, register_user, delete_registered_user
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.constructor_page import ConstructorPage
from pages.profile_page import ProfilePage


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
def unique_user_payload():
    return generate_random_user_data()


@pytest.fixture
def registered_user(unique_user_payload):

    response = register_user(unique_user_payload)
    data = response.json()

    unique_user_payload["accessToken"] = data.get("accessToken")

    yield unique_user_payload

    token = unique_user_payload.get("accessToken")
    if token:
        delete_registered_user(token)


@pytest.fixture
def log_in_account(login_page, registered_user):
    login_page.login(registered_user['email'], registered_user['password'])
    return login_page


@pytest.fixture
def constructor_page(log_in_account):
    constructor_page = ConstructorPage(log_in_account.driver)
    constructor_page.wait_open()
    return constructor_page


@pytest.fixture
def profile_page(constructor_page):
    constructor_page.navigate_to_personal_account()
    profile_page = ProfilePage(constructor_page.driver)
    profile_page.wait_open()
    return profile_page


@pytest.fixture
@allure.step('Кликнуть "Личный кабинет" на главной странице')
def login_page(driver):
    login_page = LoginPage(driver)
    login_page.open()

    return login_page


@pytest.fixture
@allure.step('Кликнуть "Восстановить пароль" на странице логина в Личный кабинет')
def forgot_password_page(login_page):
    login_page.click_forgot_password_link()
    forgot_password_page = ForgotPasswordPage(login_page.driver)

    return forgot_password_page
