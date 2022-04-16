from selenium.webdriver.common.by import By


class DashboardPage:
	LEFT_COLUMN = (By.XPATH, "//*[@class='list-group-item']")
	PRODUCT_NAME = (By.XPATH, "//h2")
	PRODUCT_COMPARE = (By.ID, "compare-total")
	PRODUCT_CARD = (By.XPATH, "//*[@class='product-layout product-grid col-lg-4 col-md-4 col-sm-6 col-xs-12']")
	ADD_TO_CARD = (By.XPATH, "//*[@class='button-group']//*[@type='button'][1]")
