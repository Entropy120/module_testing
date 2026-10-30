def test_cookie_management(browser):
    browser.get("https://the-internet.herokuapp.com/")

    browser.add_cookie({"name": "test_cookie", "value": "12345"})

    cookies = browser.get_cookies()
    cookie_names = [c['name'] for c in cookies]
    assert "test_cookie" in cookie_names

    browser.delete_all_cookies()
    assert len(browser.get_cookies()) == 0
