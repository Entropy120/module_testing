from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput


class BaseMobilePage:
    def __init__(self, driver):
        self.driver = driver

    def swipe(self, start_x_pct, start_y_pct, end_x_pct, end_y_pct, duration=800):
        """
        Универсальный свайп с использованием W3C Actions.
        Координаты задаются в процентах от ширины и высоты экрана (от 0.0 до 1.0).
        """
        # Получаем размер экрана устройства
        size = self.driver.get_window_size()

        # Вычисляем координаты в пикселях
        start_x = size['width'] * start_x_pct
        start_y = size['height'] * start_y_pct
        end_x = size['width'] * end_x_pct
        end_y = size['height'] * end_y_pct

        # Настраиваем W3C Actions (современный стандарт Appium)
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))

        # Сценарий жеста: нажать -> подождать -> сдвинуть -> отпустить
        actions.w3c_actions.pointer_action.move_to_location(start_x, start_y)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(duration / 1000)
        actions.w3c_actions.pointer_action.move_to_location(end_x, end_y)
        actions.w3c_actions.pointer_action.release()

        # Выполняем жест
        actions.perform()