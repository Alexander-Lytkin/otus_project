import allure
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from seven_homework.page_objets.RegistrationPage import RegistrationPage


@allure.title("Проверка наличия элементов на странице регистрации")
@pytest.mark.skip(reason="use only with local opencard")
def test_check_registration_page_elements(browser):
    browser.get(browser.url + "/index.php?route=account/register")
    wait = WebDriverWait(browser, 5)
    assert wait.until(EC.visibility_of_element_located(RegistrationPage.INPUT_FIRST_NAME))
    assert wait.until(EC.visibility_of_element_located(RegistrationPage.INPUT_LAST_NAME))
    assert wait.until(EC.visibility_of_element_located(RegistrationPage.INPUT_EMAIL))
    assert wait.until(EC.visibility_of_element_located(RegistrationPage.INPUT_PHONE))
    assert wait.until(EC.visibility_of_element_located(RegistrationPage.INPUT_PASSWORD))
    assert wait.until(EC.visibility_of_element_located(RegistrationPage.INPUT_PASSWORD_CONFIRM))
    assert wait.until(EC.visibility_of_element_located(RegistrationPage.PRIVACY_POLICY))
    assert wait.until(EC.visibility_of_element_located(RegistrationPage.SUBMIT_BUTTON))
