import pytest
import allure
from selenium import webdriver
from helpers.constants import BASE_URL


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и закрытия браузера.
    """
    driver = init_driver()
    open_page(driver, BASE_URL)

    yield driver

    quit_driver(driver)


@allure.step('Открываем браузер Firefox')
def init_driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    return driver


@allure.step('Открываем страницу {page}')
def open_page(driver, page):
    driver.get(page)


@allure.step('Закрываем браузер')
def quit_driver(driver):
    driver.quit()
