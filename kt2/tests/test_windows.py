from selenium.webdriver.common.by import By


def test_switch_to_new_window(browser):
    browser.get("https://the-internet.herokuapp.com/windows")

    main_window = browser.current_window_handle

    browser.find_element(By.LINK_TEXT, "Click Here").click()

    all_windows = browser.window_handles
    assert len(all_windows) == 2, "Новое окно не открылось"

    for window in all_windows:
        if window != main_window:
            browser.switch_to.window(window)
            break

    assert "New Window" in browser.find_element(By.TAG_NAME, "h3").text

    browser.switch_to.window(main_window)
    assert "Opening a new window" in browser.find_element(By.TAG_NAME, "h3").text
