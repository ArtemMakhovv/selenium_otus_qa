import pytest

from pages.admin_login_page import AdminLoginPage
from pages.admin_dashboard_page import AdminDashboardPage


class TestAdminLoginPage:

    USERNAME = 'user'
    PASSWORD = 'bitnami'

    @pytest.fixture
    def prepare_page(self, browser, url):
        browser.get(url + "/admin")
        self.login_page = AdminLoginPage(browser)
        self.admin_dashboard = AdminDashboardPage(browser)

    def test_check_login_page_elements(self, prepare_page):
        self.login_page.get_element(self.login_page.LOGIN_HEADER, 2)
        self.login_page.get_element(self.login_page.USERNAME_TEXT_BOX)
        self.login_page.get_element(self.login_page.PASSWORD_TEXT_BOX)
        self.login_page.get_element(self.login_page.LOGIN_BUTTON)
        self.login_page.get_element(self.login_page.FORGOTTEN_PASSWORD_LINK)

    def test_admin_panel_login_logout(self, prepare_page):
        self.login_page.login(self.USERNAME, self.PASSWORD)
        self.login_page.wait_title('Dashboard')

        self.admin_dashboard.logout()
        self.login_page.wait_title('Administration')




