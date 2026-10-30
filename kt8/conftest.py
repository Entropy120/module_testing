import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture(scope="session")
def browser():
    options = Options()

    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--user-agent=Automation QA (Windows NT 6.1; rv:106.0) Gecko/20100101 Firefox/106.0")
    options.page_load_strategy = "normal"

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()


    driver.wait = WebDriverWait(driver, 10, poll_frequency=1)

    yield driver
    driver.quit()
    # pip install selenium pytest Pillow
    # pytest tests/ -v