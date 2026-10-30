from appium.webdriver.common.appiumby import AppiumBy
from pages.base_mobile_page import BaseMobilePage


class CatalogPage(BaseMobilePage):
    PRODUCT_TITLE = (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'Sauce Labs')]")

    def is_product_visible(self, product_name):
        """Проверяет, виден ли товар на экране в данный момент"""
        elements = self.driver.find_elements(*self.PRODUCT_TITLE)
        for el in elements:
            if product_name in el.text:
                return True
        return False
