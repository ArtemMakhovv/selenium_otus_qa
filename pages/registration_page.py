from pages.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By


class RegistrationPage(BasePage):

    FIRST_NAME_TEXT_BOX = (By.XPATH, "//input[@name='firstname']")
    LAST_NAME_TEXT_BOX = (By.XPATH, "//input[@name='lastname']")
    EMAIL_TEXT_BOX = (By.XPATH, "//input[@name='email']")
    TELEPHONE_TEXT_BOX = (By.XPATH, "//input[@name='telephone']")
    PASSWORD = (By.XPATH, "//input[@name='password']")

    def __init__(self, driver: webdriver):
        super().__init__(driver)
