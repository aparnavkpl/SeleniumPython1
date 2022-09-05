import time

import pytest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

from PageObjects.RegisterSecuritizer import Login

driver = None


@pytest.fixture(scope="class")
def setup(request):
    global driver
    service_obj = Service("/Users/Aparna/Downloads/chromedriver_win32/chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)
    driver.maximize_window()
    base = 'http://pinglend.dev/#/login'
    driver.get(base)
    login_to_pinglend(driver)
    request.cls.driver = driver
    yield
    driver.close()


def login_to_pinglend(driver):
    driver = driver
    login = Login(driver)
    login.Login_username().send_keys("admin@email.com")
    login.Login_SignIn().click()
    time.sleep(5)
    login.Login_password().send_keys("pinglend")
    login.Login_SignIn().click()
    time.sleep(5)
