import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", choices=["chrome", "firefox"])
    parser.addoption("--headless", action="store_true", help="Запуск в фоне")


@pytest.fixture(scope="function")  
def browser(request):
    browser_name = request.config.getoption("--browser")
    is_headless = request.config.getoption("--headless")

    if browser_name == "firefox":
        options = FirefoxOptions()
        if is_headless:
            options.add_argument("--headless")
    else:
        options = ChromeOptions()
        if is_headless:
            options.add_argument("--headless")


    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4444',  # Адрес нашего хаба
        options=options
    )

    driver.maximize_window()
    yield driver
    driver.quit()
    # pip install selenium pytest pytest-xdist
    # winget install EclipseAdoptium.Temurin.17.JDK
    # java -jar selenium-server-4.27.0.jar standalone --selenium-manager true (terminal1)
    # pytest tests/test_grid.py -n 2 --browser chrome (terminal2)