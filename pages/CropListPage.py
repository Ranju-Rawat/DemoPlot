from selenium.webdriver.common.by import By


class cropList():

    def __init__(self, driver):
        self.driver = driver

    addCrop = (By.CSS_SELECTOR, ".cropBtn")
    seasonTxt = (By.XPATH, "(//input[@id = 'season-name'])[1]")
    seasons = (By.XPATH, "//ul[@id= 'season-name-listbox']/li")
    yearTxt = (By.CSS_SELECTOR, "#current-year")
    yrsList = (By.XPATH, "//ul[@id='current-year-listbox']/li")
    cropName = (By.XPATH, "(//input[@id = 'crop-name'])[1]")
    cropList = (By.XPATH, "//ul[@id='crop-name-listbox']/li")
    filterCrop = (By.XPATH, "//tr[@class='MuiTableRow-root css-1gqug66']/td[text()='Okra']")
    uploadFile = (By.XPATH, "(//p[@class='uploadButton'])[1]")

    def getAddButton(self):
        return self.driver.find_element(*cropList.addCrop)

    def getSeasonTxt(self):
        return self.driver.find_element(*cropList.seasonTxt)

    def getSeasons(self):
        return self.driver.find_elements(*cropList.seasons)

    def getYearTxt(self):
        return self.driver.find_element(*cropList.yearTxt)

    def getYrsList(self):
        return self.driver.find_elements(*cropList.yrsList)

    def getCropNm(self):
        return self.driver.find_element(*cropList.cropName)

    def getCropList(self):
        return self.driver.find_elements(*cropList.cropList)

    def getFilteredCrop(self):
        return self.driver.find_element(*cropList.filterCrop)

    def getUploadFile(self):
        return self.driver.find_element(*cropList.uploadFile)
