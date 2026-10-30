import pytest
from selenium import webdriver


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
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()

    driver.maximize_window()
    yield driver
    driver.quit()
    # pip install selenium pytest
    # pytest -v