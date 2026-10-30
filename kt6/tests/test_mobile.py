from pages.mobile_pages import LoginPage, CatalogPage


def test_successful_mobile_login(mobile_driver):
    login_page = LoginPage(mobile_driver)


    (login_page
     .enter_username("bod@example.com")
     .enter_password("10203040")
     .click_login())


    catalog_page = CatalogPage(mobile_driver)
    assert catalog_page.is_loaded(), "Не удалось войти в приложение или каталог не загрузился"

    def test_unsuccessful_mobile_login(mobile_driver):
        login_page = LoginPage(mobile_driver)


        (login_page
         .enter_username("bod@example.com")
         .enter_password("wrong_password_123")
         .click_login())


        assert login_page.is_error_displayed(), "Ожидалось сообщение об ошибке, но его нет!"