from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from locators.base import SPINNER

WAIT_TIMEOUT = 3


class BasePage:
    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(driver, WAIT_TIMEOUT)

    def scroll_to_element(self, element: WebElement) -> WebElement:
        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);", element)
        return self.wait_element_visible(element)

    def wait_element_visible(self, element: WebElement) -> WebElement:
        return self.wait.until(
            expected_conditions.visibility_of(element))

    def wait_element_invisible(self, locator) -> None:
        self.wait.until(
            expected_conditions.invisibility_of_element_located(locator))

    def wait_element_clickable(self, element: WebElement) -> WebElement:
        self.wait_element_invisible(SPINNER)
        return self.wait.until(
            expected_conditions.element_to_be_clickable(element))

    def find_element_with_scroll(self, locator: tuple) -> WebElement:
        return self.scroll_to_element(self.driver.find_element(*locator))

    def click_element(self, element: WebElement):
        self.wait_element_clickable(element)
        element.click()

    def fill_input(self, locator: tuple, value: str):
        element = self.find_element_with_scroll(locator)
        element.send_keys(value)

    def find_element_in_block(self, block: WebElement, locator: tuple) -> WebElement:
        return self.scroll_to_element(block.find_element(*locator))

    def wait_change_url(self, url: str):
        self.wait.until(expected_conditions.url_to_be(url))

    def is_open_(self, url, locator) -> bool:
        try:
            self.wait_change_url(url)
            self.find_element_with_scroll(locator)
            return True
        except TimeoutError, NoSuchElementException:
            return False
