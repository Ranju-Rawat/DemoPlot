from selenium.webdriver.common.by import By


class addCrop():

    def __init__(self, driver):
        self.driver = driver


    yearTxt = (By.CSS_SELECTOR, "#years")
    yrsList = (By.XPATH, "//ul[@id = 'years-listbox']/li")
    seasonTxt = (By.XPATH, "(//input[@id = 'season-name'])[2]")
    seasons = (By.XPATH, "//ul[@id= 'season-name-listbox']/li")
    cropName = (By.XPATH, "(//input[@id = 'crop-name'])[2]")
    submit = (By.CLASS_NAME, "saveButton")
    successMsg = (By.CLASS_NAME, "go3958317564")
    errorMsg = (By.CSS_SELECTOR, "span[class = 'error']")
    cancel = (By.XPATH, "//div[@class= 'modal-container']/div/p")

    def entYrTxt(self):
        return self.driver.find_element(*addCrop.yearTxt)

    def getYrsList(self):
        return self.driver.find_elements(*addCrop.yrsList)

    def getSeasonTxt(self):
        return self.driver.find_element(*addCrop.seasonTxt)

    def getSeasons(self):
        return self.driver.find_elements(*addCrop.seasons)

    def getCropNm(self):
        return self.driver.find_element(*addCrop.cropName)

    def getSubmit(self):
        return self.driver.find_element(*addCrop.submit)

    def getErrMsg(self):
        return self.driver.find_element(*addCrop.errorMsg)

    def getCancelButton(self):
        return self.driver.find_element(*addCrop.cancel)

