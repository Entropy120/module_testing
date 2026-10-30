import time
from pages.dropdown_page import DropdownPage
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By


def test_dropdown_select_methods(browser):
    page = DropdownPage(browser)
    page.open()
    dropdown = page.get_select_object()


    dropdown.select_by_visible_text("Option 1")
    assert dropdown.first_selected_option.text == "Option 1"


    dropdown.select_by_value("2")
    assert dropdown.first_selected_option.text == "Option 2"


    dropdown.select_by_index(1)
    assert dropdown.first_selected_option.text == "Option 1"


def test_dropdown_iterate_all_options(browser):
    page = DropdownPage(browser)
    page.open()
    dropdown = page.get_select_object()


    all_options = dropdown.options
    for option in all_options:
        if option.get_attribute("value") != "":
            dropdown.select_by_value(option.get_attribute("value"))
            time.sleep(0.5)


def test_multiselect(browser):

    browser.get("https://demoqa.com/select-menu")
    multi_select_element = browser.find_element(By.ID, "cars")
    multi_select = Select(multi_select_element)

    assert multi_select.is_multiple is True

    multi_select.select_by_visible_text("Volvo")
    multi_select.select_by_visible_text("Audi")

    selected_texts = [opt.text for opt in multi_select.all_selected_options]
    assert "Volvo" in selected_texts
    assert "Audi" in selected_texts