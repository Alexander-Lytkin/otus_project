import allure
from selenium.webdriver.common.by import By
from seven_homework.common.random import *
from seven_homework.page_objets.BasePage import BasePage


class RegistrationPage(BasePage):
    INPUT_FIRST_NAME = (By.XPATH, "//*[@id='input-firstname']")
    INPUT_LAST_NAME = (By.XPATH, "//*[@id='input-lastname']")
    INPUT_EMAIL = (By.XPATH, "//*[@id='input-email']")
    INPUT_PHONE = (By.XPATH, "//*[@id='input-telephone']")
    INPUT_PASSWORD = (By.XPATH, "//*[@id='input-password']")
    INPUT_PASSWORD_CONFIRM = (By.XPATH, "//*[@id='input-confirm']")
    PRIVACY_POLICY = (By.XPATH, "//*[@type='checkbox']")
    SUBMIT_BUTTON = (By.XPATH, "//*[@type='submit']")
    CREATED_ACCOUNT_TITLE = (By.XPATH, "//*[@id='content']//h1")

    REGISTRATION_API = "?route=account/register"

    def __init__(self, browser, password=None):
        super().__init__(browser)
        self.browser = browser
        self.password = password
    
    @allure.step
    def open_registration_card(self):
        return self.browser.get(self.browser.url + self.REGISTRATION_API)

    @allure.step
    def input_registration_fields(self):
        data = {
            "firstname": random_first_name(),
            "lastname": random_second_name(),
            "email": random_email(),
            "telephone": random_phone(),
            "password": random_password(),
        }
        for element in [self.INPUT_FIRST_NAME, self.INPUT_LAST_NAME, self.INPUT_EMAIL, self.INPUT_PHONE,
                        self.INPUT_PASSWORD, self.INPUT_PASSWORD_CONFIRM]:
            key = (data.get(element[1][15:-2]))

            element = self._element(element)

            if element.accessible_name == "Password":
                self.password = key

            if element.accessible_name == "Password Confirm":
                element.send_keys(self.password)
            else:
                element.send_keys(key)
    
    @allure.step
    def agree_policy(self):
        self._click(self.PRIVACY_POLICY)
    
    @allure.step
    def press_submit_button(self):
        self._click(self.SUBMIT_BUTTON)
    
    @allure.step
    def check_success_registration_account(self):
        self._verify_element_presence(self.CREATED_ACCOUNT_TITLE)
