import os
from selenium.webdriver.common.by import By


def test_responsive_layout(browser):
    browser.get("https://www.saucedemo.com/")

    os.makedirs("screenshots", exist_ok=True)

    size = browser.get_window_size()
    screen_name = f"{size['width']}x{size['height']}"

    browser.save_screenshot(f"screenshots/screen_{screen_name}.png")

    username_field = browser.find_element(By.ID, "user-name")
    login_button = browser.find_element(By.ID, "login-button")

    assert username_field.is_displayed(), "Поле логина не видно на этом разрешении!"
    assert login_button.is_displayed(), "Кнопка входа не видна на этом разрешении!"
