from five_homework.page_objets.MainPage import MainPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_check_main_page_elements(browser):
    browser.get(browser.url)
    wait = WebDriverWait(browser, 5)
    wait.until(EC.visibility_of_element_located(MainPage.TITLE))
    wait.until(EC.visibility_of_element_located(MainPage.TOP_MENU))
    wait.until(EC.visibility_of_element_located(MainPage.FEATURED_TITLE))
    wait.until(EC.visibility_of_element_located(MainPage.TOP_SLIDER))
    wait.until(EC.visibility_of_element_located(MainPage.BOTTOM_SLIDER))
    wait.until(EC.visibility_of_all_elements_located(MainPage.FEATURED_CARDS))
