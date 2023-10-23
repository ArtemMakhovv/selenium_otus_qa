from pages.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By


class ProductPage(BasePage):

    ADD_TO_CART_BTN = (By.XPATH, "//*[@id='button-cart']")
    DESCRIPTION_TAB_BTN = (By.XPATH, "//a[text()='Description']")
    SPECIFICATION_TAB_BTN = (By.XPATH, "//a[text()='Specification']")
    REVIEWS_TAB_BTN = (By.XPATH, "//a[contains(text(),'Reviews')]")
    ADD_WISH_LIST_BTN = (By.XPATH, "//button[@data-original-title='Add to Wish List']")

    def __init__(self, driver: webdriver):
        super().__init__(driver)
