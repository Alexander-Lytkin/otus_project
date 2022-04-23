import allure
from selenium.webdriver.common.by import By
from seven_homework.page_objets.BasePage import BasePage


class MainPage(BasePage):
    CURRENCY = (By.XPATH, "//*[contains(text(), 'Currency')]")
    CURRENT_CURRENCY = (By.XPATH, "//*[@class='btn btn-link dropdown-toggle']")
    CURRENCY_LIST = (By.XPATH, "//*[@class='currency-select btn btn-link btn-block']")
    TITLE = (By.TAG_NAME, "//title")

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    @property
    def current_currency(self):
        return self.browser.find_element(By.XPATH, self.CURRENT_CURRENCY[1])

    @property
    def all_currency_list(self):
        elements = self.browser.find_elements(By.XPATH, self.CURRENCY_LIST[1])
        return elements

    @property
    def currency_button(self):
        element = self._element(self.CURRENCY)
        return element

    @allure.step
    def choose_currency(self, currency):
        element = self.currency_button
        element.click()
        value = [el for el in self.all_currency_list if el.accessible_name == currency]
        value[0].click()
