import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput


def swipe(driver, start_x_pct, start_y_pct, end_x_pct, end_y_pct, duration=800):
    """Универсальный свайп по процентам от размера экрана"""
    size = driver.get_window_size()
    start_x = size['width'] * start_x_pct
    start_y = size['height'] * start_y_pct
    end_x = size['width'] * end_x_pct
    end_y = size['height'] * end_y_pct

    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))

    actions.w3c_actions.pointer_action.move_to_location(start_x, start_y)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.pause(duration / 1000)
    actions.w3c_actions.pointer_action.move_to_location(end_x, end_y)
    actions.w3c_actions.pointer_action.release()

    actions.perform()


def test_swipe_down_catalog(mobile_driver):
    mobile_driver.implicitly_wait(5)

    bottom_item = (By.XPATH, "//*[@text='Sauce Labs Onesie']")

    swipe(mobile_driver, start_x_pct=0.5, start_y_pct=0.8, end_x_pct=0.5, end_y_pct=0.2, duration=1000)

    elements_after = mobile_driver.find_elements(*bottom_item)
    is_visible_after = any(el.is_displayed() for el in elements_after)

    assert is_visible_after is True, "Свайп не сработал, нижний товар не появился"
