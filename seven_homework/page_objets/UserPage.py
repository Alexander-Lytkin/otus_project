from selenium.webdriver.common.by import By
from .elements.UserLoginForm import UserLoginForm
from .BasePage import BasePage


class UserPage(BasePage):
	PAYMENT_FORM = (By.CSS_SELECTOR, "#payment-new")
	
	def login_with(self, username, password):
		UserLoginForm(self.browser).login_with(username, password)
	
	def click_link(self, link_text):
		self._click((By.LINK_TEXT, link_text))
	
	def verify_pay_form(self):
		self._verify_element_presence(self.PAYMENT_FORM)
	
	def verify_product_link(self, product_name):
		self._verify_link_presence(product_name)
