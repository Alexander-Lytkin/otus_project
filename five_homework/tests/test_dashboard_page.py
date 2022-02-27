from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from five_homework.page_objets.DashboardPage import DashboardPage


def test_check_dashboard_page_elements(browser):
    browser.get(browser.url + "/index.php?route=product/category&path=20_27")
    wait = WebDriverWait(browser, 5)
    wait.until(EC.presence_of_all_elements_located(DashboardPage.LEFT_COLUMN))
    wait.until(EC.visibility_of_element_located(DashboardPage.PRODUCT_NAME))
    wait.until(EC.visibility_of_element_located(DashboardPage.PRODUCT_COMPARE))
    wait.until(EC.visibility_of_element_located(DashboardPage.PRODUCT_CARD))
    wait.until(EC.visibility_of_element_located(DashboardPage.ADD_TO_CARD))
