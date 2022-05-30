from selenium.webdriver.common.by import By

from page_objets.BasePage import BasePage


class CartPage(BasePage):
    BUTTONS = (By.CSS_SELECTOR, ".buttons")
    CHECKOUT_LINK = (By.LINK_TEXT, "Checkout")
    CONTENT = (By.CSS_SELECTOR, "#content")

    def go_to_checkout(self):
        self._click_in_element(self._element(self.BUTTONS), self.CHECKOUT_LINK)

    def verify_product(self, product_name):
        self._verify_element_presence(self.CONTENT)
        self._verify_link_presence(product_name)
        return self
