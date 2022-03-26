from seven_homework.page_objets.BasePage import BasePage
from selenium.webdriver.common.by import By


class SuccessRegistrationPage(BasePage):
    CREATED_ACCOUNT_TITLE = (By.XPATH, "//*[@id='content']//h1")

    REGISTRATION_API = "?route=account/register"

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def check_success_registration_account(self):
        return self._verify_element_presence(self.CREATED_ACCOUNT_TITLE)
