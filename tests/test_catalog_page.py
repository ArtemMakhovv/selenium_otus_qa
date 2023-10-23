import pytest

from pages.catalog_page import CatalogPage


class TestCatalogPage:

    @pytest.fixture
    def prepare_page(self, browser, url):
        browser.get(url + "/desktops")
        self.catalog_page = CatalogPage(browser)

    def test_check_catalog_page_elements(self, prepare_page):
        self.catalog_page.get_element(self.catalog_page.PRODUCTS_MENU, 2)
        self.catalog_page.get_element(self.catalog_page.GRID_VIEW_BTN, 1)
        self.catalog_page.get_element(self.catalog_page.LIST_VIEW_BTN)
        self.catalog_page.get_element(self.catalog_page.PRODUCTS_SHOW_LIMIT_DROPDOWN)
        self.catalog_page.get_element(self.catalog_page.PRODUCTS_SORT_DROPDOWN)

    def test_change_currency(self, prepare_page):
        self.catalog_page.change_currency('EUR')
        product_cur = self.catalog_page.get_element_text(self.catalog_page.PRODUCT_PRICE)

        assert '€' in product_cur
