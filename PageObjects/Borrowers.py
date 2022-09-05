from selenium.webdriver.common.by import By


class Borrowers:

    def __init__(self, driver):
        self.driver = driver

    BorrowersTab = (By.XPATH, "//div[text()='Borrowers']")
    SearchTextBox = (By.XPATH, "//input[@placeholder='Search']")

    def Borrowers_tab(self):
        return self.driver.find_element(*Borrowers.BorrowersTab)

    def Borrowers_SearchTextBox(self):
        return self.driver.find_element(*Borrowers.SearchTextBox)


