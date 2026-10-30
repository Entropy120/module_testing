from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH_MESSAGE = (By.ID, "flash")

    def enter_username(self, username):
        element = self.wait.until(EC.visibility_of_element_located(self.USERNAME_FIELD))
        element.clear()
        element.send_keys(username)
        return self

    def enter_password(self, password):
        element = self.wait.until(EC.visibility_of_element_located(self.PASSWORD_FIELD))
        element.clear()
        element.send_keys(password)
        return self

    def click_login_button(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()
        return self

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
        return self

    def get_flash_message(self):
        element = self.wait.until(EC.visibility_of_element_located(self.FLASH_MESSAGE))
        return element.text
