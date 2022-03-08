import pytest
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.firefox.service import Service as FFService
import mysql.connector


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--url", default="https://demo.opencart.com")
    parser.addoption("--drivers", action="store",
                     default=os.path.expanduser("~/PycharmProjects/OTUS/otus_project/five_homework/drivers"))


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    drivers = request.config.getoption("--drivers")

    if browser == "chrome":
        service = ChromiumService(executable_path=drivers + "/chromedriver")
        driver = webdriver.Chrome(service=service)
    elif browser == "firefox":
        service = FFService(executable_path=drivers + "/geckodriver")
        driver = webdriver.Firefox(service=service)
    elif browser == "opera":
        driver = webdriver.Opera(executable_path=drivers + "/operadriver")
    else:
        driver = webdriver.Safari()

    driver.maximize_window()

    request.addfinalizer(driver.close)

    driver.get(url)
    driver.url = url

    return driver


@pytest.fixture
def db_connection(request):
    connection = mysql.connector.connect(
        user='bn_opencart',
        password='',
        host='127.0.0.1',
        database='bitnami_opencart',
        port='3306'
    )
    request.addfinalizer(connection.close)
    return connection
