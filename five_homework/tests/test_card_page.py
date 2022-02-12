from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from five_homework.pages.CardPage import CardPage


def test_check_card_page_elements(browser):
    browser.get(browser.url + "/index.php?route=product/product&product_id=40")
    wait = WebDriverWait(browser, 5)
    wait.until(EC.visibility_of_element_located(CardPage.WISH_LIST_BUTTON))
    wait.until(EC.visibility_of_element_located(CardPage.COMPARE_BUTTON))
    wait.until(EC.visibility_of_element_located(CardPage.PRODUCT_NAME))
    wait.until(EC.visibility_of_element_located(CardPage.ADD_BUTTON))
    wait.until(EC.visibility_of_all_elements_located(CardPage.SHORT_PRODUCT_LIST))
