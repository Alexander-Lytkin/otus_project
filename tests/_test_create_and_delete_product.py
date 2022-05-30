import allure
import pytest

from page_objets import MainPage, RegistrationPage
from page_objets.elements.SuccessLogin import SuccessRegistrationPage


@allure.title("Создание нового аккаунта")
@pytest.mark.skip(reason="use only with web opencard")
def test_registration_new_account(browser):
	registration_page = RegistrationPage(browser)
	registration_page.open_registration_card()
	registration_page.input_registration_fields()
	registration_page.agree_policy()
	registration_page.press_submit_button()
	success_reg_page = SuccessRegistrationPage(browser)
	assert success_reg_page.check_success_registration_account().text == "Your Account Has Been Created!"


@allure.title("Смена валюты на главной странице")
def test_change_currency(browser):
	main_page = MainPage(browser)
	main_page.choose_currency("€ Euro")
	assert main_page.current_currency.text == "€ Currency "


@allure.title("Падающий тест при смене валюты на главной странице")
def test_change_currency_failed(browser):
	main_page = MainPage(browser)
	main_page.choose_currency("€ Euro")
	assert main_page.current_currency.text == "$ Currency "
