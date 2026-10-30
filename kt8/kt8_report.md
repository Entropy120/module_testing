# Отчет по практической работе: Dropdown, Multiselect, Keyboard и Screenshot Testing

## 1. Конфигурация тестового окружения
Для работы использовался Selenium WebDriver с настроенными опциями:
- Отключен флаг автоматизации (`--disable-blink-features=AutomationControlled`).
- Установлен кастомный User-Agent.
- Стратегия загрузки страницы: `normal`.

## 2. Работа с Dropdown и Multiselect
В ходе работы был использован класс `Select` из `selenium.webdriver.support.select`.
Были реализованы и проверены следующие методы:
- `select_by_visible_text()` — выбор по тексту.
- `select_by_value()` — выбор по атрибуту value.
- `select_by_index()` — выбор по порядковому номеру.
- Итерация по всем элементам списка через атрибут `options`.
- Демонстрация Multiselect (на примере demoqa.com): выбор нескольких элементов и проверка через `all_selected_options`.

## 3. Работа с клавиатурой
Для эмуляции нажатий использовался модуль `Keys`. 
Реализован кроссплатформенный подход:
```python
os_name = platform.system()
CMD_CTRL = Keys.COMMAND if os_name == "Darwin" else Keys.CONTROL