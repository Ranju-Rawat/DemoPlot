import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Utilities.BaseClass import BaseClass
from pages.CropListPage import cropList
from pages.AdvUpload import uploadFiles
from pages.addCropPage import addCrop


class TestAddCrop(BaseClass):

    def test_ValidateCropForm(self):
        cropListPage = cropList(self.driver)
        cropBtn = cropListPage.getAddButton()
        addCropPg = addCrop(self.driver)
        wait = WebDriverWait(self.driver, 5)
        wait.until(expected_conditions.element_to_be_clickable(cropBtn)).click()
        wait.until(expected_conditions.element_to_be_clickable(addCropPg.getSubmit())).click()
        ErrMsg = wait.until(expected_conditions.visibility_of(addCropPg.getErrMsg())).text
        assert "Mandatory" in ErrMsg
        time.sleep(5)
        wait.until(expected_conditions.element_to_be_clickable(addCropPg.getCancelButton())).click()
        print(ErrMsg)


    def test_cropAdd(self):
        cropListPage = cropList(self.driver)
        cropBtn = cropListPage.getAddButton()
        addCropPg = addCrop(self.driver)
        wait = WebDriverWait(self.driver, 5)
        wait.until(expected_conditions.element_to_be_clickable(cropBtn)).click()
        wait.until(expected_conditions.element_to_be_clickable(addCropPg.entYrTxt())).send_keys("2024")
        years = wait.until(expected_conditions.presence_of_all_elements_located(addCropPg.yrsList))
        print(years)
        for year in years:
            if "2024" in year.text:
                year.click()

        wait.until(expected_conditions.element_to_be_clickable(addCropPg.getSeasonTxt())).send_keys("rabi")
        seasons = wait.until(expected_conditions.presence_of_all_elements_located(addCropPg.seasons))
        for season in seasons:
            if "Rabi" in season.text:
                season.click()

        wait.until(expected_conditions.element_to_be_clickable(addCropPg.getCropNm())).send_keys("Okra")
        wait.until(expected_conditions.element_to_be_clickable(addCropPg.getSubmit())).click()
        SuccessMsg = wait.until(expected_conditions.visibility_of_element_located(addCropPg.successMsg)).text
        assert "Crop Added Successfully" == SuccessMsg
        print("Message", SuccessMsg)
        time.sleep(5)

    def test_FilterList(self):
        cropListPage = cropList(self.driver)
        uploadPg = uploadFiles(self.driver)
        wait = WebDriverWait(self.driver, 5)
        wait.until(expected_conditions.element_to_be_clickable(cropListPage.getSeasonTxt())).send_keys("Rabi")
        seasonList = wait.until(expected_conditions.presence_of_all_elements_located(cropListPage.seasons))
        for season in seasonList:
            if "Rabi" in season.text:
                season.click()

        wait.until(expected_conditions.element_to_be_clickable(cropListPage.getYearTxt())).send_keys("2024")
        years = wait.until(expected_conditions.presence_of_all_elements_located(cropListPage.yrsList))
        for year in years:
            if "2024" in year.text:
                year.click()

        wait.until(expected_conditions.element_to_be_clickable(cropListPage.getCropNm())).send_keys("Okra")
        crops = wait.until(expected_conditions.presence_of_all_elements_located(cropListPage.cropList))
        for crop in crops:
            if "Okra" in crop.text:
                crop.click()

        filteredCrop = wait.until(expected_conditions.visibility_of_element_located(cropListPage.filterCrop)).text
        assert "Okra" == filteredCrop

        wait.until(expected_conditions.element_to_be_clickable(cropListPage.getUploadFile())).click()
        print(filteredCrop)

        #file_Adv = wait.until(expected_conditions.element_to_be_clickable(uploadPg.getUploadAdv()))
        file_Adv = uploadPg.getUploadAdv()
        file_Adv.send_keys("C:\\Users\\rawat\\Downloads\\advisory without error.xlsx")
        file_Nutrient = uploadPg.getUploadNutrient()
        file_Nutrient.send_keys("C:\\Users\\rawat\\Downloads\\test crop three nutrient without error.xlsx")

        wait.until(expected_conditions.element_to_be_clickable(uploadPg.getUploadButton())).click()
        print("Done")
        time.sleep(10)



