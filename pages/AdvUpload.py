from selenium.webdriver.common.by import By


class uploadFiles():

    def __init__(self, driver):
        self.driver = driver


    #uploadAdvisory = (By.XPATH, "(//div[@class='uploadFile'])[1]")
    uploadAdvisory = (By.XPATH, "(//input[@type='file'])[1]")
    uploadNutrient = (By.XPATH, "(//input[@type='file'])[2]")
    uploadButton = (By.CLASS_NAME, "saveButton")

    def getUploadAdv(self):
        return self.driver.find_element(*uploadFiles.uploadAdvisory)

    def getUploadNutrient(self):
        return self.driver.find_element(*uploadFiles.uploadNutrient)

    def getUploadButton(self):
        return self.driver.find_element(*uploadFiles.uploadButton)