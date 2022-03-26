from selenium.webdriver.common.by import By

from ..BasePage import BasePage


class UserLoginForm(BasePage):
    INPUT_EMAIL = (By.CSS_SELECTOR, "#input-email")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input[value=Login]")

    def login_with(self, username, password):
        self._element(self.INPUT_EMAIL).send_keys(username)
        self._element(self.INPUT_PASSWORD).send_keys(password)
        self._element(self.LOGIN_BUTTON).click()
