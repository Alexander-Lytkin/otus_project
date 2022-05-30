import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from page_objets.LoginPage import LoginAdminPage


@allure.title("Проверка наличия элементов страницы для входа")
def test_check_admin_page_elements(browser):
    browser.get(browser.url + "/admin/")
    wait = WebDriverWait(browser, 5)
    assert wait.until(EC.visibility_of_element_located(LoginAdminPage.LOGO))
    assert wait.until(EC.visibility_of_element_located(LoginAdminPage.PANEL_TITLE))
    assert wait.until(EC.visibility_of_element_located(LoginAdminPage.INPUT_USERNAME))
    assert wait.until(EC.visibility_of_element_located(LoginAdminPage.INPUT_PASSWORD))
    assert wait.until(EC.visibility_of_element_located(LoginAdminPage.FORGOTTEN_PASSWORD_BUTTON))
    assert wait.until(EC.visibility_of_element_located(LoginAdminPage.LOGIN_BUTTON))
