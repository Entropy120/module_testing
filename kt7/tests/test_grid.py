from selenium.webdriver.common.by import By


def test_title_check(browser):
    browser.get("https://the-internet.herokuapp.com/")
    assert "The Internet" in browser.title


def test_windows(browser):
    browser.get("https://the-internet.herokuapp.com/windows")
    browser.find_element(By.LINK_TEXT, "Click Here").click()
    assert len(browser.window_handles) == 2


def test_iframe(browser):
    browser.get("https://the-internet.herokuapp.com/iframe")
    iframe = browser.find_element(By.ID, "mce_0_ifr")
    browser.switch_to.frame(iframe)

    editor = browser.find_element(By.ID, "tinymce")
    editor.clear()
    editor.send_keys("Grid Test")



    assert editor.is_displayed()

    browser.switch_to.default_content()