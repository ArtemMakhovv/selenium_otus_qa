from pages.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By


class AdminDashboardPage(BasePage):

    LOGOUT_BTN = (By.XPATH, "//span[text()='Logout']")

    def __init__(self, driver: webdriver):
        super().__init__(driver)

    def logout(self):
        self.get_element_and_click(self.LOGOUT_BTN)
