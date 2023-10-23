from pages.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By


class CatalogPage(BasePage):

    PRODUCTS_MENU = (By.XPATH, "//*[@class='list-group']")
    PRODUCTS_SORT_DROPDOWN = (By.XPATH, "//select[@id='input-sort']")
    PRODUCTS_SHOW_LIMIT_DROPDOWN = (By.XPATH, "//*[@id='input-limit']")
    LIST_VIEW_BTN = (By.XPATH, "//button[@id='list-view']")
    GRID_VIEW_BTN = (By.XPATH, "//button[@id='grid-view']")
    CURRENCY_BTN = (By.XPATH, "//form[@id='form-currency']//button[@class='btn btn-link dropdown-toggle']")
    PRODUCT_PRICE = (By.XPATH, "//p[@class='price']")

    def __init__(self, driver: webdriver):
        super().__init__(driver)

    def change_currency(self, currency: str):
        currency_item = (By.XPATH, f"//button[@name='{currency}']")
        self.get_element_and_click(self.CURRENCY_BTN)
        self.get_element_and_click(currency_item)
        