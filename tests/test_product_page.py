import pytest

from pages.product_page import ProductPage


class TestProductPage:

    @pytest.fixture
    def prepare_page(self, browser, url):
        browser.get(url + '/macbook')
        self.product_page = ProductPage(browser)

    def test_check_product_page_elements(self, prepare_page):
        self.product_page.get_element(self.product_page.ADD_WISH_LIST_BTN, 2)
        self.product_page.get_element(self.product_page.ADD_TO_CART_BTN, 1)
        self.product_page.get_element(self.product_page.REVIEWS_TAB_BTN)
        self.product_page.get_element(self.product_page.DESCRIPTION_TAB_BTN)
        self.product_page.get_element(self.product_page.SPECIFICATION_TAB_BTN)
