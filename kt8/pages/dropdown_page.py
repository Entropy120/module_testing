from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class DropdownPage:
    def __init__(self, driver):
        self.driver = driver
        self.dropdown_locator = (By.ID, "dropdown")

    def open(self):
        self.driver.get("http://the-internet.herokuapp.com/dropdown")

    def get_select_object(self):

        element = self.driver.find_element(*self.dropdown_locator)
        return Select(element)