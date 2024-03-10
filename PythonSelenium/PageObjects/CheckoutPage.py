from selenium.webdriver.common.by import By


class CheckOutPage :

    def __init__(self, driver):
        self.driver = driver

    phoneNm = (By.XPATH, "//div[@class = 'card h-100']")
    button = (By.CSS_SELECTOR, "a[class = 'nav-link btn btn-primary")
    successButton = (By.XPATH, "//button[@class = 'btn btn-success']")
    dropdown = (By.CSS_SELECTOR, "#country")
    countries = (By.XPATH, "//div[@class='suggestions']/ul/li")
    checkBox = (By.CSS_SELECTOR, "div[class='checkbox checkbox-primary']")
    purchase = (By.CSS_SELECTOR, "input[value='Purchase']")
    successMsg = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")


    #phone = (By.XPATH, "div/h4/a")


    def phoneList(self):
        return self.driver.find_elements(*CheckOutPage.phoneNm)

    # def getPhone(self):
    #     return self.driver.find_element(CheckOutPage.phone)

    def getButton(self):
        return self.driver.find_element(*CheckOutPage.button)

    def getSuccessButton(self):
        return self.driver.find_element(*CheckOutPage.successButton)

    def getDropDown(self):
        return self.driver.find_element(*CheckOutPage.dropdown)

    def getCountries(self):
        return self.driver.find_element(*CheckOutPage.countries)

    def getCheckbox(self):
        return self.driver.find_element(*CheckOutPage.checkBox)

    def getPurchase(self):
        return self.driver.find_element(*CheckOutPage.purchase)

    def getSuccessMsg(self):
        return self.driver.find_element(*CheckOutPage.successMsg)

