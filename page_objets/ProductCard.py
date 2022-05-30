from selenium.webdriver.common.by import By

from page_objets.AdminPage import AdminPage


class ProductCard(AdminPage):
    # PRODUCT CARD
    GENERAL_TAB = (By.XPATH, "//*[@id='form-product']//*[@href='#tab-general']")
    DATA_TAB = (By.XPATH, "//*[@id='form-product']//*[@href='#tab-data']")
    PRODUCT_NAME = (By.XPATH, "//*[@placeholder='Product Name']")
    PRODUCT_TAG = (By.XPATH, "//*[@placeholder='Meta Tag Title']")
    MODEL = (By.XPATH, "//*[@placeholder='Model']")
    SAVE_BUTTON = (By.XPATH, "//*[@data-original-title='Save']")
    EMPTY_PRODUCT_TABLE = (By.XPATH, "//*[text()='No results!']")

    def __init__(self, browser):
        super().__init__(browser)

    def fill_product_name(self):
        self._element(self.PRODUCT_NAME).send_keys("TEST_PRODUCT")
        self._element(self.PRODUCT_TAG).send_keys("test_data")

    def open_data_tab(self):
        self._element(self.DATA_TAB).click()

    def fill_model_name(self):
        self.open_data_tab()
        self._element(self.MODEL).send_keys("TEST_MODEL")

    def save_product(self):
        self._element(self.SAVE_BUTTON).click()

    def check_empty_product_list(self):
        return self._element(self.EMPTY_PRODUCT_TABLE).text
