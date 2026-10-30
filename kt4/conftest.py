import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", choices=["chrome", "firefox"])

    parser.addoption("--headless", action="store_true", help="Запуск браузера в фоновом режиме")


@pytest.fixture(scope="session")
def browser(request):
    browser_name = request.config.getoption("--browser")
    is_headless = request.config.getoption("--headless")

    if browser_name == "firefox":
        options = FirefoxOptions()

        options.add_argument("--width=1280")
        options.add_argument("--height=800")

        if is_headless:
            options.add_argument("--headless")

        driver = webdriver.Firefox(options=options)
    else:
        options = ChromeOptions()

        options.add_argument("--window-size=1280,800")

        options.add_argument("--ignore-certificate-errors")

        options.add_argument("--incognito")
        if is_headless:
            options.add_argument("--headless")

        driver = webdriver.Chrome(options=options)

    driver.implicitly_wait(5)
    yield driver
    driver.quit()
   # pip install selenium pytest
   # pytest tests/ -v
   # pytest tests/ -v --headless