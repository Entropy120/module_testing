from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseMobilePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

class LoginPage(BaseMobilePage):

    USERNAME_FIELD = (By.ID, "com.saucelabs.mydemoapp.android:id/nameET")
    PASSWORD_FIELD = (By.ID, "com.saucelabs.mydemoapp.android:id/passwordET")
    LOGIN_BUTTON = (By.ID, "com.saucelabs.mydemoapp.android:id/loginBtn")

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

    def click_login(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()
        return self

class CatalogPage(BaseMobilePage):

    PRODUCTS_TITLE = (By.XPATH, "//android.widget.TextView[@text='Products']")

    def is_loaded(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.PRODUCTS_TITLE))
            return True
        except Exception:
            return False