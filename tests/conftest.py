import datetime
import logging
import os

import allure
import mysql.connector
import pytest
from selenium import webdriver

from tests.page_objets.AdminPage import AdminPage


def pytest_addoption(parser):
	parser.addoption("--browser", action="store", default="chrome", choices=["chrome", "firefox", "opera"])
	parser.addoption("--executor", action="store", default="localhost")
	parser.addoption("--url", action="store", default="https://demo-opencart.com")
	parser.addoption("--bversion", default=None)
	parser.addoption("--vnc", default=False)
	parser.addoption("--log_level", action="store", default="DEBUG")
	parser.addoption("--drivers", action="store",
	                 default=os.path.expanduser("/drivers"))


@pytest.fixture
def browser(request):
	browser = request.config.getoption("--browser")
	executor = request.config.getoption("--executor")
	url = request.config.getoption("--url")
	version = request.config.getoption("--bversion")
	vnc = request.config.getoption("--vnc")
	log_level = request.config.getoption("--log_level")
	drivers = request.config.getoption("--drivers")
	
	logger = logging.getLogger('driver')
	test_name = request.node.name
	
	logger.info("===> Test {} started at {}".format(test_name, datetime.datetime.now()))
	
	if executor == "local":
		caps = {'goog:chromeOptions': {}}
		driver = webdriver.Chrome(desired_capabilities=caps, executable_path=drivers + "/chromedriver")
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
	
	# driver = EventFiringWebDriver(driver, MyListener())
	driver.test_name = test_name
	driver.log_level = log_level
	
	logger.info("Browser:{}".format(browser, driver.desired_capabilities))
	
	def fin():
		driver.quit()
		logger.info("===> Test {} finished at {}".format(test_name, datetime.datetime.now()))
	
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
	with open(f'{tests_root}/allure-results/environment.properties', 'w') as f:
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
	if rep.when == 'call' and rep.failed:
		mode = 'a' if os.path.exists('failures') else 'w'
		try:
			with open('failures', mode) as f:
				if 'browser' in item.fixturenames:
					web_driver = item.funcargs['browser']
				else:
					print('Fail to take screen-shot')
					return
			allure.attach(
				web_driver.get_screenshot_as_png(),
				name='screenshot',
				attachment_type=allure.attachment_type.PNG
			)
		except Exception as e:
			print('Fail to take screen-shot: {}'.format(e))
