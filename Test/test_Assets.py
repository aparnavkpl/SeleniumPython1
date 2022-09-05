import time
import pytest
from PageObjects.Assets import Assets
from TestData.AssetsData import AssetsSearchData
from utilities.BaseClass import BaseClass


class TestAssets(BaseClass):

    try:

        def test_AssetsSearchItem(self, getData):
            assets = Assets(self.driver)
            assets.Assets_tab().click()
            time.sleep(2)
            assets.Assets_SearchTextBox().send_keys(getData["searchText"])
            time.sleep(5)
            self.driver.refresh()

        @pytest.fixture(params=AssetsSearchData.assets_search_data)
        def getData(self, request):
            return request.param

    except Exception as e:
        print(e)
