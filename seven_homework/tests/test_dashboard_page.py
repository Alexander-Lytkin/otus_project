import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from seven_homework.page_objets.DashboardPage import DashboardPage


@allure.title("Проверка наличия элементов страницы витрины")
def test_check_dashboard_page_elements(browser):
    browser.get(browser.url + "/index.php?route=product/category&path=20_27")
    wait = WebDriverWait(browser, 5)
    assert wait.until(EC.presence_of_all_elements_located(DashboardPage.LEFT_COLUMN))
    assert wait.until(EC.visibility_of_element_located(DashboardPage.PRODUCT_NAME))
    assert wait.until(EC.visibility_of_element_located(DashboardPage.PRODUCT_COMPARE))
    assert wait.until(EC.visibility_of_element_located(DashboardPage.PRODUCT_CARD))
    assert wait.until(EC.visibility_of_element_located(DashboardPage.ADD_TO_CARD))
