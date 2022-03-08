import time

from five_homework.page_objets.AdminPage import AdminPage
from five_homework.page_objets.MainPage import MainPage
from five_homework.page_objets.RegistrationPage import RegistrationPage
from five_homework.page_objets.elements.SuccessLogin import SuccessRegistrationPage


# Добавление нового товара в разделе администратора.
# Удаление товара из списка в разделе администартора.

def test_add_new_item(browser):
    admin_page = AdminPage(browser)
    admin_page.open_admin_page()
    admin_page.login()
    # browser.get(browser.url + "/admin/")

    pass


def test_remove_item(browser):
    pass


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
    main_page.choose_currency("€ Euro")
    assert main_page.current_currency.text == "€ Currency "
