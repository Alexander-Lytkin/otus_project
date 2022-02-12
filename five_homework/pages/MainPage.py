from selenium.webdriver.common.by import By


class MainPage:
    TITLE = (By.ID, "logo")
    TOP_MENU = (By.XPATH, "//*[@class='nav navbar-nav']")
    FEATURED_TITLE = (By.TAG_NAME, "h3")
    TOP_SLIDER = (By.XPATH, "//*[@id='common-home']//*[@class='swiper-viewport'][1]")
    FEATURED_CARDS = (By.XPATH, "//*[@class='product-thumb transition']")
    BOTTOM_SLIDER = (By.XPATH, "//*[@id='common-home']//*[@class='swiper-viewport'][2]")
