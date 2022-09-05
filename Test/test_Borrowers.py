import time
import pytest
from PageObjects.Borrowers import Borrowers
from TestData.BorrowersData import BorrowersSearchData
from utilities.BaseClass import BaseClass


class TestBorrowers(BaseClass):

    try:

        def test_BorrowersSearchUser(self, getData):
            borrowers = Borrowers(self.driver)
            borrowers.Borrowers_tab().click()
            time.sleep(2)
            borrowers.Borrowers_SearchTextBox().send_keys(getData["searchText"])
            time.sleep(5)
            self.driver.refresh()

        @pytest.fixture(params=BorrowersSearchData.borrowers_search_data)
        def getData(self, request):
            return request.param

    except Exception as e:
        print(e)
