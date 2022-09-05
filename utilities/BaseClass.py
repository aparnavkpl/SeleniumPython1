import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageObjects.RegisterSecuritizer import Login


@pytest.mark.usefixtures("setup")
class BaseClass:
    def verifyElementPresent(self, xpath):
        elem = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )

    def selectValueFromDropdown(self, dropdowntext, element):
        print(dropdowntext)
        for option in element:
            if dropdowntext in option.text:
                print(option.text)
                self.driver.execute_script("arguments[0].click();", option)
                break


