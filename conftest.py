import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--max", action="store_true")
    parser.addoption("--url", help="base application url")


@pytest.fixture(scope="session")
def browser_name(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def browser(browser_name, request):

    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "safari":
        driver = webdriver.Safari()
    elif browser_name == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError(f"Browser {browser_name} not supported.")

    if request.config.getoption("--max"):
        driver.maximize_window()

    yield driver
    driver.quit()
