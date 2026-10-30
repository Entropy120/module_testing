import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options


@pytest.fixture(scope="function")
def mobile_driver():
    options = UiAutomator2Options()
    options.platform_name = 'Android'

    #  Замените 'R58M12345' на ID вашего телефона, который показала команда adb devices
    options.device_name = 'F6EU65KFHANZ4XNJ'
    options.udid = 'F6EU65KFHANZ4XNJ'  # Рекомендуется указывать udid

    options.automation_name = 'UiAutomator2'


    options.app = r'C:\Users\entro\Desktop\module_testing\kt6\mda-2.2.0-25.apk'


    driver = webdriver.Remote('http://127.0.0.1:4723', options=options)

    yield driver

    driver.quit()
    # winget install OpenJS.NodeJS.LTS
    # pip install pytest appium-python-client
    # npm install -g appium
    # appium driver install uiautomator2
    # appium (terminal1)
    # pytest tests/test_mobile.py -v (terminal2)
    # https://developer.android.com/studio#command-line-tools-only