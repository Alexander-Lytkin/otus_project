from selenium.webdriver.common.by import By

from five_homework.page_objets.BasePage import BasePage


class MainPage(BasePage):
    CURRENCY = (By.XPATH, "//*[contains(text(), 'Currency')]")
    CURRENCY_LIST = (By.XPATH, "//*[@class='currency-select btn btn-link btn-block']")

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def click_featured_product(self, number):
        index = number - 1
        feature_product = self.browser.find_elements(By.CSS_SELECTOR, "#content > div.row .product-layout")[index]
        product_name = feature_product.find_element(By.CSS_SELECTOR, ".caption h4 a").text
        feature_product.click()
        return product_name

    def find_currency(self):
        element = self._element(self.CURRENCY)
        return element

    def choose_currency(self, currency):
        element = self.find_currency()
        element.click()

        all_currency = self._click_in_element(element, self.CURRENCY_LIST, 1)
