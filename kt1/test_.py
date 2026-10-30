def test_example(browser):
    browser.get("http://www.google.com")
    assert "Google" in browser.title
    # pytest --browser firefox
    # pytest --browser chrome