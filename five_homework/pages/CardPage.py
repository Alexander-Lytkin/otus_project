from selenium.webdriver.common.by import By


class CardPage:
    WISH_LIST_BUTTON = (
        By.XPATH, "//*[@data-toggle='tooltip'][@data-original-title='Add to Wish List'][@class='btn btn-default']")
    COMPARE_BUTTON = (
        By.XPATH, "//*[@data-toggle='tooltip'][@data-original-title='Compare this Product'][@class='btn btn-default']")
    PRODUCT_NAME = (By.XPATH, "//*[@class='row']//*[@class='col-sm-4']/h1")
    SHORT_PRODUCT_LIST = (By.XPATH, "//*[@class='row']//*[@class='col-sm-4']//*[@class='list-unstyled'][1]")
    ADD_BUTTON = (By.XPATH, "//*[@id='button-cart']")
