import pytest

from pages.registration_page import RegistrationPage


class TestRegisterPage:

    @pytest.fixture
    def prepare_page(self, browser, url):
        browser.get(url + '/index.php?route=account/register')
        self.register_page = RegistrationPage(browser)

    def test_check_register_page_elements(self, prepare_page):
        self.register_page.get_element(self.register_page.FIRST_NAME_TEXT_BOX, 2)
        self.register_page.get_element(self.register_page.LAST_NAME_TEXT_BOX, 1)
        self.register_page.get_element(self.register_page.EMAIL_TEXT_BOX)
        self.register_page.get_element(self.register_page.TELEPHONE_TEXT_BOX)
        self.register_page.get_element(self.register_page.PASSWORD)
