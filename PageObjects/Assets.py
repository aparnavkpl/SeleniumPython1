from selenium.webdriver.common.by import By


class Assets:

    def __init__(self, driver):
        self.driver = driver

    AssetsTab = (By.XPATH, "//div[text()='Assets']")
    SearchTextBox = (By.XPATH, "//input[@placeholder='Search']")

    def Assets_tab(self):
        return self.driver.find_element(*Assets.AssetsTab)

    def Assets_SearchTextBox(self):
        return self.driver.find_element(*Assets.SearchTextBox)


