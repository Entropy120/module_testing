import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

SCREEN_SIZES = [
    pytest.param((1920, 1080), id="Desktop"),
    pytest.param((768, 1024), id="Tablet"),
    pytest.param((375, 812), id="Mobile")
]


@pytest.fixture(scope="function", params=SCREEN_SIZES)
def browser(request):
    width, height = request.param

    options = Options()
    options.add_argument(f"--window-size={width},{height}")

    options.add_argument("--disable-notifications")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
# pip install pytest-html
# pytest tests/test_responsive.py -v --html=report.html --self-contained-html