from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver: webdriver):
        self.driver = driver

    def get_element(self, locator, wait_time=1):
        try:
            element = WebDriverWait(self.driver, wait_time).until(EC.visibility_of_element_located(locator))
            return element
        except TimeoutException:
            raise AssertionError(f"Элемент:{locator} не найден на странице за {wait_time} секунд")

    def get_element_and_click(self, locator, wait_time=1):
        self.get_element(locator, wait_time).click()

    def element_send_keys(self, locator, input_text: str, wait_time=1):
        self.get_element(locator, wait_time).send_keys(input_text)

    def get_element_text(self, locator, wait_time=1):
        return self.get_element(locator, wait_time).text

    def wait_title(self, title, wait_time=1):
        try:
            WebDriverWait(self.driver, wait_time).until(EC.title_is(title))
        except TimeoutException:
            raise AssertionError(f"Ожидаемый title: '{title}', текущий: '{self.driver.title}'")
