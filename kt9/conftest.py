import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions


def pytest_addoption(parser):
    parser.addoption("--platform", action="store", default="android", choices=["android", "ios"])


@pytest.fixture(scope="session")
def mobile_driver(request):
    platform = request.config.getoption("--platform")

    if platform == "ios":
        options = XCUITestOptions()
        options.platform_name = 'iOS'
        options.device_name = 'iPhone 14'
        options.automation_name = 'XCUITest'
        options.app = 'my_app.ipa'
    else:
        options = UiAutomator2Options()
        options.platform_name = 'Android'
        options.device_name = 'F6EU65KFHANZ4XNJ'
        options.automation_name = 'UiAutomator2'
        options.app_package = 'com.saucelabs.mydemoapp.android'
        options.app_activity = 'com.saucelabs.mydemoapp.android.view.activities.SplashActivity'
        options.set_capability("appium:ignoreHiddenApiPolicyError", True)

    driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
    yield driver
    driver.quit()
    # pip install pytest appium-python-client
    # appium (terminal1)
    # pytest tests/test_swipe.py -v (terminal2)
