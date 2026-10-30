import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        choices=["chrome", "firefox"],
        help="Браузер для запуска тестов: chrome или firefox",
    )


@pytest.fixture(scope="session")
def browser(request):
    browser_name = request.config.getoption("--browser")

    if browser_name == "firefox":
        driver = webdriver.Firefox(options=FirefoxOptions())
    else:
        driver = webdriver.Chrome(options=ChromeOptions())

    driver.maximize_window()
    driver.implicitly_wait(5)

    yield driver

    driver.quit()
    # pip install selenium pytest
    # pytest tests/ -v