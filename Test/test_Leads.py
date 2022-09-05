import time
import pytest
from PageObjects.Leads import Leads
from TestData.LeadsData import LeadsSearchData
from utilities.BaseClass import BaseClass


class TestLeads(BaseClass):

    try:

        def test_LeadsSearchUser(self, getData):
            leads = Leads(self.driver)
            leads.Leads_tab().click()
            time.sleep(2)
            leads.Leads_SearchTextBox().send_keys(getData["searchText"])
            time.sleep(5)
            self.driver.refresh()

        @pytest.fixture(params=LeadsSearchData.leads_search_data)
        def getData(self, request):
            return request.param

    except Exception as e:
        print(e)
