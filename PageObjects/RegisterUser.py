from selenium.webdriver.common.by import By


class RegisterUser:

    def __init__(self, driver):
        self.driver = driver

    registerUser = (By.XPATH, '//div[text()="Register User"]')
    identityDropdown = (By.XPATH, "//div[@class='q-field__native row items-center']")
    identityDropdownOptions = (By.XPATH, "//div[@role='option']//div[@class='q-item__label']//span")
    Fname = (By.XPATH, '//input[@aria-label="First Name"]')
    Lname = (By.XPATH, '//input[@aria-label="Last Name"]')
    Email = (By.XPATH, '//input[@aria-label="Email Address"]')
    MobileNumber = (By.XPATH, '//input[@aria-label="Mobile Phone"]')
    password1 = (By.XPATH, '(//input[@type="password"])[1]')
    confirmPass = (By.XPATH, '(//input[@type="password"])[2]')
    submit = (By.XPATH, '//button[@type="submit"]')

    def RegisterUser_tab(self):
        return self.driver.find_element(*RegisterUser.registerUser)

    def RegisterUser_IdentityDropdown(self):
        return self.driver.find_element(*RegisterUser.identityDropdown)

    def RegisterUser_DropdownValue(self):
        return self.driver.find_elements(*RegisterUser.identityDropdownOptions)

    def RegisterUser_Fname(self):
        return self.driver.find_element(*RegisterUser.Fname)

    def RegisterUser_Lname(self):
        return self.driver.find_element(*RegisterUser.Lname)

    def RegisterUser_Email(self):
        return self.driver.find_element(*RegisterUser.Email)

    def RegisterUser_MobileNumber(self):
        return self.driver.find_element(*RegisterUser.MobileNumber)

    def RegisterUser_password1(self):
        return self.driver.find_element(*RegisterUser.password1)

    def RegisterUser_ConfirmPass(self):
        return self.driver.find_element(*RegisterUser.confirmPass)

    def RegisterUser_Submit(self):
        return self.driver.find_element(*RegisterUser.submit)


