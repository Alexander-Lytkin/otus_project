import os

import allure
import mysql.connector
import pytest
from selenium import webdriver

from seven_homework.page_objets.AdminPage import AdminPage


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", choices=["chrome", "firefox", "opera"])
    parser.addoption("--executor", action="store", default="192.168.10.149")
    parser.addoption("--url", default="https://demo-opencart.com/")
    parser.addoption("--bversion", default=None)
    parser.addoption("--vnc", default=False)


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    url = request.config.getoption("--url")
    version = request.config.getoption("--bversion")
    vnc = request.config.getoption("--vnc")

    if executor == "local":
        caps = {'goog:chromeOptions': {}}
        driver = webdriver.Chrome(desired_capabilities=caps)
    else:
        executor_url = f"http://{executor}:4444/wd/hub"

        caps = {
            "browserName": browser,
            "browserVersion": version,
            "screenResolution": "1280x720",
            "name": "Alexander",
            "selenoid:options": {
                "enableVNC": vnc,
            },
            'acceptSslCerts': True,
            'acceptInsecureCerts': True,
            'timeZone': 'Europe/Moscow',
            'goog:chromeOptions': {}
        }
        driver = webdriver.Remote(
            command_executor=executor_url,
            desired_capabilities=caps
        )
        driver.maximize_window()
        driver.get(url)
        driver.url = url
            
    def fin():
        driver.quit()

    request.addfinalizer(fin)
    return driver
    
    
@pytest.fixture(scope="session", autouse=True)
def get_environment(pytestconfig):
    props = {
        'Browser': 'Chrome',
        'Browser.Version': '98.0',
        'Stand': 'Production',
        'Shell': os.getenv('SHELL')
    }

    tests_root = pytestconfig.rootdir
    with open(f'{tests_root}/seven_homework/tests/allure-results/environment.properties', 'w') as f:
        env_props = '\n'.join([f'{k}={v}' for k, v in props.items()])
        f.write(env_props)


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


@pytest.fixture
def admin_page(browser):
    admin_page = AdminPage(browser)
    admin_page.open_admin_page()
    admin_page.login()
    admin_page.choose_product_catalog()
    return admin_page


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.failed is True:
        web_driver = item.funcargs['browser']
        allure.attach(
            web_driver.get_screenshot_as_png(),
            name='SCREENSHOT',
            attachment_type=allure.attachment_type.PNG
        )
