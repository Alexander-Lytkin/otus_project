from selenium.webdriver.common.by import By

from five_homework.page_objets.BasePage import BasePage


class AdminPage(BasePage):
    # LOGIN CREDITS
    ADMIN_USERNAME = (By.XPATH, "//*[@id='input-username']")
    ADMIN_PASSWORD = (By.XPATH, "//*[@id='input-password']")
    LOGIN_BUTTON = (By.XPATH, "//*[@class='btn btn-primary']")
    USERNAME = "user"
    PASSWORD = "bitnami"

    # ADMIN_PAGE
    CATALOG = (By.XPATH, "//*[@href='#collapse1']")
    ADD_NEW_PRODUCT_BUTTON = (By.XPATH, "//*[@data-original-title='Add New']")
    DELETE_BUTTON = (By.XPATH, "//*[@data-original-title='Delete']")
    PRODUCTS_TAB = (By.XPATH, "//*[@id='collapse1']//*[contains(text(), 'Products')]")
    SUCCESS_ALERT = (By.XPATH, "//*[@class='alert alert-success alert-dismissible']")

    # FILTER
    PRODUCT_NAME_FILTER = (By.XPATH, "//*[@id='input-name']")
    FILTER_BUTTON = (By.XPATH, "//*[@id='button-filter']")

    # FILTER RESULT
    FILTER_RESULT = (By.XPATH, "//tbody//*[@alt='TEST_PRODUCT']")

    # CHECK BOXES
    SELECT_ALL_CHECK_BOXES = (By.XPATH, "//*[@type='checkbox'][@onclick]")

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

    def choose_product_catalog(self):
        self._element(self.CATALOG).click()
        self._element(self.PRODUCTS_TAB).click()

    def create_new_product(self):
        self._element(self.ADD_NEW_PRODUCT_BUTTON).click()

    @property
    def check_alert_text(self):
        return self._element(self.SUCCESS_ALERT).text.split("\n")[0]

    def find_created_product(self):
        self._element(self.PRODUCT_NAME_FILTER).send_keys("TEST_PRODUCT")
        self._element(self.FILTER_BUTTON).click()

    def check_filter_result(self):
        self._element(self.FILTER_RESULT)

    def select_all_products(self):
        self._element(self.SELECT_ALL_CHECK_BOXES).click()

    def press_delete_button(self):
        self._element(self.DELETE_BUTTON).click()

    def delete_created_product(self):
        self.check_filter_result()
        self.select_all_products()
        self.press_delete_button()
