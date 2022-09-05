import time
import pytest
from PageObjects.Securitizers import Securitizers
from TestData.AssetsData import AssetsSearchData
from utilities.BaseClass import BaseClass


class TestSecuritizers(BaseClass):

    try:

        def test_SecuritizersSearchItem(self, getData):
            securitizers = Securitizers(self.driver)
            securitizers.Securitizers_tab().click()
            time.sleep(2)
            securitizers.Securitizers_SearchTextBox().send_keys(getData["searchText"])
            time.sleep(5)
            self.driver.refresh()

        @pytest.fixture(params=AssetsSearchData.assets_search_data)
        def getData(self, request):
            return request.param

    except Exception as e:
        print(e)
