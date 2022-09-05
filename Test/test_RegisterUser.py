import time
import pytest
from PageObjects.RegisterUser import RegisterUser
from TestData.RegisterUserData import RegisterUserData
from utilities.BaseClass import BaseClass


class TestRegisterUser(BaseClass):

    try:

        def test_registerUser(self, getData):
            registerUser = RegisterUser(self.driver)
            registerUser.RegisterUser_tab().click()
            time.sleep(2)
            registerUser.RegisterUser_IdentityDropdown().click()
            time.sleep(4)
            AllOptions = registerUser.RegisterUser_DropdownValue()
            DropDownValue = getData["IdentityValue"]
            print(DropDownValue)
            self.selectValueFromDropdown(DropDownValue, AllOptions)
            registerUser.RegisterUser_Fname().send_keys(getData["Fname"])
            registerUser.RegisterUser_Lname().send_keys(getData["Lname"])
            registerUser.RegisterUser_Email().send_keys(getData["Email"])
            registerUser.RegisterUser_MobileNumber().send_keys(getData["MobileNumber"])
            registerUser.RegisterUser_password1().send_keys(getData["Password1"])
            registerUser.RegisterUser_ConfirmPass().send_keys(getData["ConfirmPass"])
            registerUser.RegisterUser_Submit().click()
            self.driver.refresh()

        @pytest.fixture(params=RegisterUserData.register_user_data)
        def getData(self, request):
            return request.param

    except Exception as e:
        print(e)
