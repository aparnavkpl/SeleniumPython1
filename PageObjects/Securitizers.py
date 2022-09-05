from selenium.webdriver.common.by import By


class Securitizers:

    def __init__(self, driver):
        self.driver = driver

    SecuritizersTab = (By.XPATH, "//div[text()='Securitizers']")
    SearchTextBox = (By.XPATH, "//input[@placeholder='Search']")

    def Securitizers_tab(self):
        return self.driver.find_element(*Securitizers.SecuritizersTab)

    def Securitizers_SearchTextBox(self):
        return self.driver.find_element(*Securitizers.SearchTextBox)


