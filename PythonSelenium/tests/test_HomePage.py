import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from PageObjects.HomePage import HomePage
from testData.HomePageData import HomePageData
from utilities.baseClass import BaseClass


class TestHomePg(BaseClass):

    def test_formSubmittion(self, getData):
        # sObj = Service("\\Users\\rawat\\Downloads\\chromedriver-win64\\chromedriver.exe")
        # driver = webdriver.Chrome(service=sObj)
        # driver.get("https://rahulshettyacademy.com/angularpractice/")
        time.sleep(5)
        log = self.test_loggingDemo()
        homePG = HomePage(self.driver)
        log.info(getData["Name"])
        homePG.getName().send_keys(getData["Name"])
        homePG.getEmail().send_keys(getData["Email"])
        homePG.getPassword().send_keys(getData["Password"])
        homePG.getCheckBox().click()
        homePG.getGender()
        self.selectOptionByText(homePG.getGender(), getData["Gender"])
        #dropdown.select_by_index(0)
        time.sleep(5)
        homePG.getSubmit().click()
        msg = homePG.getSuccessMsg().text
        assert "success" in msg
        self.driver.refresh()



        # locators in selenium - Id, xpath, cssSelector, classname, name, linktext, partialLinktext, tagname
        # driver.find_element(By.XPATH, "//input[@class='form-control ng-pristine ng-invalid ng-touched']").send_keys("Ranju Rawat")
        # driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
        # driver.find_element(By.ID, "exampleInputPassword1").send_keys("12345")
        # driver.find_element(By.ID, "exampleCheck1").click()
        # # For static dropdown

        # xpath = //tagname[@attribute = "value"]
        # driver.find_element(By.XPATH, "//input[@type='submit']").click()
        # msg = driver.find_element(By.CLASS_NAME, "alert-success").text
        #
        # print(msg)
        # assert "success" in msg

    @pytest.fixture(params=HomePageData.test_HomePage_Data)
    def getData(self, request):
        return request.param


