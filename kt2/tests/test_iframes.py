from selenium.webdriver.common.by import By


def test_iframe_text_editor(browser):
    browser.get("https://the-internet.herokuapp.com/iframe")

    iframe_element = browser.find_element(By.ID, "mce_0_ifr")
    browser.switch_to.frame(iframe_element)

    editor_body = browser.find_element(By.ID, "tinymce")
    editor_body.clear()
    editor_body.send_keys("Автоматизация iframe успешна!")

    browser.switch_to.default_content()

    assert "An iFrame containing the TinyMCE WYSIWYG Editor" in browser.find_element(By.TAG_NAME, "h3").text
