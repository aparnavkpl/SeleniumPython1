from selenium.webdriver.common.by import By


class Leads:

    def __init__(self, driver):
        self.driver = driver

    LeadsTab = (By.XPATH, "//div[text()='Leads']")
    SearchTextBox = (By.XPATH, "//input[@placeholder='Search']")

    def Leads_tab(self):
        return self.driver.find_element(*Leads.LeadsTab)

    def Leads_SearchTextBox(self):
        return self.driver.find_element(*Leads.SearchTextBox)


