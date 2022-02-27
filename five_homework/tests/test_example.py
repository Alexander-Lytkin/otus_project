from five_homework.page_objets.MainPage import MainPage
from five_homework.page_objets.RegistrationPage import RegistrationPage
from five_homework.page_objets.elements.SuccessLogin import SuccessRegistrationPage


def test_registration_new_account(browser):
    registration_page = RegistrationPage(browser)
    registration_page.open_registration_card()
    registration_page.input_registration_fields()
    registration_page.agree_policy()
    registration_page.press_submit_button()
    success_reg_page = SuccessRegistrationPage(browser)
    assert success_reg_page.check_success_registration_account().text == "Your Account Has Been Created!"


def test_change_currency(browser):
    main_page = MainPage(browser)
    # main_page.find_currency()
    main_page.choose_currency("Euro")
# Регистрация нового пользователя в магазине опенкарта.+
# Добавление нового товара в разделе администратора.
# Удаление товара из списка в разделе администартора.
# Переключение валют из верхнего меню опенкарта.
