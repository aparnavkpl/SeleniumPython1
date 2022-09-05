import time
import pytest
from PageObjects.RegisterSecuritizer import Login
from TestData.RegisterSecuritizerData import RegisterSecuritiserData
from utilities.BaseClass import BaseClass


class TestRegisterSecuritizer(BaseClass):

    try:

        def test_formFill(self, getData):
            login = Login(self.driver)
            login.Login_RegisterSecuritizer().click()
            time.sleep(5)
            login.Login_Name().send_keys(getData["name"])
            login.Login_Address().send_keys(getData["address"])
            login.Login_PhoneNumber().send_keys(getData["PhoneNumber"])
            login.Login_ZipCode().send_keys(getData["ZipCode"])
            fname = login.Login_Fname()
            self.driver.execute_script("arguments[0].scrollIntoView();", fname)
            time.sleep(2)
            login.Login_Fname().send_keys(getData["Fname"])
            login.Login_Lname().send_keys(getData["Lname"])
            login.Login_Email().send_keys(getData["Email"])
            login.Login_MobileNumber().send_keys(getData["MobileNumber"])
            login.Login_password1().send_keys(getData["Password1"])
            login.Login_ConfirmPass().send_keys(getData["ConfirmPass"])
            login.Login_Submit().click()
            time.sleep(5)
            self.driver.refresh()

        @pytest.fixture(params=RegisterSecuritiserData.test_login_data)
        def getData(self, request):
            return request.param

    except Exception as e:
        print(e)
