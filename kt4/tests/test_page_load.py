import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options





def test_normal_strategy():
    options = Options()
    options.page_load_strategy = 'normal'
    driver = webdriver.Chrome(options=options)

    driver.get("https://whatismyipaddress.com/")
    print("\n[NORMAL] Страница загружена полностью")
    driver.quit()


def test_eager_strategy():
    options = Options()
    options.page_load_strategy = 'eager'
    driver = webdriver.Chrome(options=options)

    driver.get("https://whatismyipaddress.com/")
    print("\n[EAGER] Загружен только HTML, картинки могут еще грузиться")
    driver.quit()