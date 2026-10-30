import pytest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def test_negative_element_not_found(browser):
    browser.get("https://the-internet.herokuapp.com/")

    with pytest.raises(NoSuchElementException):
        browser.find_element(By.ID, "nonexistent-element-12345")


def test_boundary_input_length(browser):
    browser.get("https://the-internet.herokuapp.com/inputs")

    input_field = browser.find_element(By.TAG_NAME, "input")

    long_number = "9" * 100
    input_field.send_keys(long_number)

    assert input_field.get_attribute("value") == long_number
