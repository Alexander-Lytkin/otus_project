from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from five_homework.page_objets.LoginPage import LoginAdminPage


def test_check_admin_page_elements(browser):
    browser.get(browser.url + "/admin/")
    wait = WebDriverWait(browser, 5)
    wait.until(EC.visibility_of_element_located(LoginAdminPage.LOGO))
    wait.until(EC.visibility_of_element_located(LoginAdminPage.PANEL_TITLE))
    wait.until(EC.visibility_of_element_located(LoginAdminPage.INPUT_USERNAME))
    wait.until(EC.visibility_of_element_located(LoginAdminPage.INPUT_PASSWORD))
    wait.until(EC.visibility_of_element_located(LoginAdminPage.FORGOTTEN_PASSWORD_BUTTON))
    wait.until(EC.visibility_of_element_located(LoginAdminPage.LOGIN_BUTTON))
