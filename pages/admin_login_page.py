from pages.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By


class AdminLoginPage(BasePage):

    USERNAME_TEXT_BOX = (By.XPATH, "//input[@name='username']")
    PASSWORD_TEXT_BOX = (By.XPATH, "//input[@name='password']")
    FORGOTTEN_PASSWORD_LINK = (By.XPATH, "//a[text()='Forgotten Password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    LOGIN_HEADER = (By.XPATH, "//h1[@class='panel-title']")

    def __init__(self, driver: webdriver):
        super().__init__(driver)

    def login(self, username: str, password: str):
        self.element_send_keys(self.USERNAME_TEXT_BOX, username)
        self.element_send_keys(self.PASSWORD_TEXT_BOX, password)
        self.get_element_and_click(self.LOGIN_BUTTON)
