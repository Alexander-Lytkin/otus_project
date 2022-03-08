from selenium.webdriver.common.by import By

from five_homework.page_objets.BasePage import BasePage


class AdminPage(BasePage):
    ADMIN_USERNAME = (By.XPATH, "//*[@id='input-username']")
    ADMIN_PASSWORD = (By.XPATH, "//*[@id='input-password']")
    LOGIN_BUTTON = (By.XPATH, "//*[@class='btn btn-primary']")
    USERNAME = "user"
    PASSWORD = "bitnami"

    def __init__(self, browser):
        super().__init__(browser)

    def open_admin_page(self):
        self.browser.get(self.browser.url + "/admin")

    def login(self):
        self._element(self.ADMIN_USERNAME).clear()
        self._element(self.ADMIN_PASSWORD).clear()

        self._element(self.ADMIN_USERNAME).send_keys(self.USERNAME)
        self._element(self.ADMIN_PASSWORD).send_keys(self.PASSWORD)
        self._element(self.LOGIN_BUTTON).click()
