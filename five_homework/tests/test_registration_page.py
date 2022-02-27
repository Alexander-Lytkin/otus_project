from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from five_homework.page_objets.RegistrationPage import RegistrationPage


def test_check_registration_page_elements(browser):
    browser.get(browser.url + "/index.php?route=account/register")
    wait = WebDriverWait(browser, 5)
    wait.until(EC.visibility_of_element_located(RegistrationPage.INPUT_FIRST_NAME))
    wait.until(EC.visibility_of_element_located(RegistrationPage.INPUT_LAST_NAME))
    wait.until(EC.visibility_of_element_located(RegistrationPage.INPUT_EMAIL))
    wait.until(EC.visibility_of_element_located(RegistrationPage.INPUT_PHONE))
    wait.until(EC.visibility_of_element_located(RegistrationPage.INPUT_PASSWORD))
    wait.until(EC.visibility_of_element_located(RegistrationPage.INPUT_PASSWORD_CONFIRM))
    wait.until(EC.visibility_of_element_located(RegistrationPage.PRIVACY_POLICY))
    wait.until(EC.visibility_of_element_located(RegistrationPage.SUBMIT_BUTTON))
