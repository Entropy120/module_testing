import platform
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait


def test_keyboard_actions(browser):
    browser.get("http://the-internet.herokuapp.com/key_presses")


    input_field = browser.find_element(By.ID, "target")
    input_field.send_keys("Hello World")


    os_name = platform.system()
    CMD_CTRL = Keys.COMMAND if os_name == "Darwin" else Keys.CONTROL


    input_field.send_keys(CMD_CTRL + "a")
    input_field.send_keys(Keys.BACKSPACE)


    body = browser.find_element(By.TAG_NAME, "body")
    ActionChains(browser).move_to_element(body).click().send_keys(Keys.ENTER).perform()


    result_locator = (By.ID, "result")
    WebDriverWait(browser, 10).until(
        lambda d: d.find_element(*result_locator).get_attribute("innerText") != ""
    )


    result_text = browser.find_element(*result_locator).get_attribute("innerText")
    assert "ENTER" in result_text.upper(), f"Ожидался текст с ENTER, но получено: {result_text}"