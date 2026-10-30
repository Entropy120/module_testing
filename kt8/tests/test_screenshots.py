import os
from PIL import Image, ImageChops


def test_screenshot_comparison(browser):
    os.makedirs("screenshots", exist_ok=True)
    baseline_path = "screenshots/baseline.png"
    current_path = "screenshots/current.png"
    diff_path = "screenshots/diff.png"

    browser.get("http://the-internet.herokuapp.com/")

    browser.save_screenshot(current_path)

    if not os.path.exists(baseline_path):
        browser.save_screenshot(baseline_path)
        print("Эталонный скриншот создан. Запустите тест еще раз для сравнения.")
        return

    image1 = Image.open(baseline_path)
    image2 = Image.open(current_path)
    diff = ImageChops.difference(image1, image2)

    if diff.getbbox():
        diff.save(diff_path)
        print(f"НАЙДЕНЫ РАЗЛИЧИЯ! Смотрите файл {diff_path}")
        assert False, "Изображения различаются"

    assert True, "Изображения идентичны"
