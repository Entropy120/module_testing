# Отчет: Кроссплатформенное тестирование мобильного приложения (Продвинутый уровень)

## 1. Выбор приложения и настройка среды
**Приложение:** SauceLabs My Demo App (доступно на Android и iOS).
**Среда:** Appium Server 2.x, Python Client, W3C Actions API.
В `conftest.py` реализована возможность выбора платформы через аргумент `--platform android` или `--platform ios`. Для Android используется драйвер `UiAutomator2Options`, для iOS — `XCUITestOptions`.

## 2. Автоматизация свайпов
Согласно лучшим практикам, для работы с жестами используется современный стандарт **W3C Actions** (вместо устаревшего `TouchAction`). 
Разработан универсальный метод `swipe()`, который принимает координаты в **процентах от размера экрана**. Это делает тест кроссплатформенным и независимым от физического разрешения экрана устройства.

## 3. Интеграция с CI/CD (GitHub Actions)
Для обеспечения автоматического запуска на облачных фермах (BrowserStack) подготовлен пайплайн. 
Пример шага в `.github/workflows/mobile_tests.yml`:
```yaml
- name: Run Appium Tests on Android
  run: |
    pytest tests/test_swipe.py --platform android
  env:
    BROWSERSTACK_USERNAME: ${{ secrets.BS_USER }}
    BROWSERSTACK_ACCESS_KEY: ${{ secrets.BS_KEY }}