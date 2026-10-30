*** Settings ***
Library    SeleniumLibrary
Variables  ../variables.py

*** Keywords ***
# --- ОБЩИЕ ШАГИ ---
Пользователь находится на странице авторизации
    Open Browser    ${BASE_URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Element Is Visible    id=user-name

# --- ШАГИ ДЛЯ ВХОДА ---
Пользователь вводит валидные данные
    Input Text    id=user-name    ${VALID_USER}
    Input Text    id=password     ${VALID_PASS}

Пользователь вводит неверный пароль
    Input Text    id=user-name    ${VALID_USER}
    Input Text    id=password     ${INVALID_PASS}

Пользователь нажимает кнопку "Войти"
    Click Button    id=login-button

Система перенаправляет на главную страницу (Dashboard)
    Wait Until Location Contains    inventory.html
    Location Should Be    https://www.saucedemo.com/inventory.html

Появляется сообщение об ошибке
    Wait Until Element Is Visible    css=h3[data-test="error"]
    Element Should Contain    css=h3[data-test="error"]    Epic sadface

# --- ШАГИ ДЛЯ КОРЗИНЫ ---
Пользователь добавляет первый товар в корзину
    Click Button    xpath=(//button[contains(text(),'Add to cart')])[1]

Пользователь открывает корзину
    Click Element    class=shopping_cart_link

В корзине отображается 1 товар
    Wait Until Element Is Visible    class=cart_item
    ${count}=    Get Element Count    class=cart_item
    Should Be Equal As Integers    ${count}    1

# --- ШАГИ ДЛЯ СОРТИРОВКИ ---
Пользователь выбирает сортировку по цене (от низкой к высокой)
    Select From List By Value    class=product_sort_container    lohi

Цены в списке идут по возрастанию
    Wait Until Element Is Visible    css=.inventory_item_name
    ${first_item}=    Get Text    css=.inventory_item_name
    Should Be Equal    ${first_item}    Sauce Labs Onesie

# --- ШАГИ ДЛЯ HEROKUAPP ---
Пользователь находится на странице с чекбоксами
    Open Browser    https://the-internet.herokuapp.com/checkboxes    ${BROWSER}
    Maximize Browser Window
    Wait Until Element Is Visible    xpath=//input[@type='checkbox']

Пользователь ставит галочку на первом чекбоксе
    Select Checkbox    xpath=(//input[@type='checkbox'])[1]

Первый чекбокс отмечен
    Checkbox Should Be Selected    xpath=(//input[@type='checkbox'])[1]

Пользователь выбирает "Option 1" из выпадающего списка
    Open Browser    https://the-internet.herokuapp.com/dropdown    ${BROWSER}
    Maximize Browser Window
    Select From List By Label    id=dropdown    Option 1

Выбран элемент "Option 1"
    ${selected}=    Get Selected List Label    id=dropdown
    Should Be Equal    ${selected}    Option 1

# --- ШАГИ ДЛЯ IFRAME (TC10) ---
Открыт сайт с iframe
    Open Browser    https://the-internet.herokuapp.com/iframe    ${BROWSER}
    Maximize Browser Window
    Wait Until Element Is Visible    id=mce_0_ifr

Пользователь переключается в iframe
    Select Frame    id=mce_0_ifr

Пользователь вводит текст "Robot Framework"
    # Кликаем по редактору, чтобы точно установить фокус
    Click Element    id=tinymce
    Clear Element Text    id=tinymce
    Input Text    id=tinymce    Robot Framework

Текст успешно введен в iframe
    ${actual_text}=    Get Text    id=tinymce
    Should Contain    ${actual_text}    Robot Framework
    Unselect Frame

    # --- ШАГИ ДЛЯ ВЫХОДА (LOGOUT) ---
Пользователь открывает боковое меню
    Click Element    id=react-burger-menu-btn

Пользователь нажимает кнопку "Logout"
    Click Element    id=logout_sidebar_link

Система возвращает на страницу авторизации
    Wait Until Location Is    https://www.saucedemo.com/
    Wait Until Element Is Visible    id=user-name