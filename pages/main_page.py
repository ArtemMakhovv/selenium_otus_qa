from pages.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By


class MainPage(BasePage):

    OPENCART_LOGO = (By.XPATH, "//*[@title='Your Store']")
    CART_LINK = (By.XPATH, "//*[@title='Shopping Cart']")
    SEARCH_TEXT_BOX = (By.XPATH, "//input[@name='search']")
    CURRENCY_BTN = (By.XPATH, "//form[@id='form-currency']//button[@class='btn btn-link dropdown-toggle']")
    CART_ITEMS_BOX = (By.XPATH, "//span[@id='cart-total']")
    PRODUCT_PRICE = (By.XPATH, "//p[@class='price']")

    def __init__(self, driver: webdriver):
        super().__init__(driver)

    def add_to_cart(self, product_title: str):
        product = (By.XPATH, f"//a[text()='{product_title}']/ancestor::div[@class='product-thumb transition']//*[@class='fa fa-shopping-cart']/..")
        self.get_element_and_click(product)

    def check_item_in_cart(self, product_title: str):
        self.get_element_and_click(self.CART_ITEMS_BOX)
        product = (By.XPATH,
                   f"//table[@class='table table-striped']//a[text()='{product_title}']")
        self.get_element(product, 2)

    def change_currency(self, currency: str):
        currency_item = (By.XPATH, f"//button[@name='{currency}']")
        self.get_element_and_click(self.CURRENCY_BTN)
        self.get_element_and_click(currency_item)
