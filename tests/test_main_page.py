import pytest

from pages.main_page import MainPage


class TestMainPage:

    @pytest.fixture
    def prepare_page(self, browser, url):
        browser.get(url)
        self.main_page = MainPage(browser)

    def test_check_main_page_elements(self, prepare_page):
        self.main_page.get_element(self.main_page.OPENCART_LOGO, 2)
        self.main_page.get_element(self.main_page.CART_LINK, 1)
        self.main_page.get_element(self.main_page.SEARCH_TEXT_BOX)
        self.main_page.get_element(self.main_page.CURRENCY_BTN)
        self.main_page.get_element(self.main_page.CART_ITEMS_BOX)

    def test_add_to_cart(self, prepare_page):
        product_title = 'MacBook'

        self.main_page.add_to_cart(product_title)
        self.main_page.get_element_text(self.main_page.CART_ITEMS_BOX)

        assert self.main_page.get_element_text(self.main_page.CART_ITEMS_BOX).startswith("1 item(s)")
        self.main_page.check_item_in_cart(product_title)

    def test_change_currency(self, prepare_page):
        self.main_page.change_currency('EUR')
        product_cur = self.main_page.get_element_text(self.main_page.PRODUCT_PRICE)

        assert '€' in product_cur

