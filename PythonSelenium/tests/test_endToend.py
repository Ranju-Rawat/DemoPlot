import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from PageObjects.CheckoutPage import CheckOutPage
from PageObjects.HomePage import HomePage
from utilities.baseClass import BaseClass


#@pytest.mark.usefixtures("setup")
class TestOne(BaseClass):
    #def __init__(self):
        #self.driver = None

    def test_e2e(self):
       homePg =  HomePage(self.driver)
       shopBtn = homePg.shopItems()
       wait = WebDriverWait(self.driver, 15)
       wait.until(expected_conditions.element_to_be_clickable(shopBtn)).click()
       checkOutPg = CheckOutPage(self.driver)
       phnList = checkOutPg.phoneList()
       log = self.test_loggingDemo()

       # phones = wait.until(expected_conditions.presence_of_all_elements_located(phnList))
       # print(phones)
       for phone in phnList:

           ph = phone.find_element(By.XPATH, "div/h4/a")
           log.info(phone.text)
           if ph.text == "Blackberry":
               phone.find_element(By.XPATH, "div/button").click()
               break

       wait.until(expected_conditions.element_to_be_clickable(checkOutPg.getButton())).click()
       wait.until(expected_conditions.element_to_be_clickable(checkOutPg.getSuccessButton())).click()
       #wait.until(expected_conditions.visibility_of_element_located(checkOutPg.getDropDown())).send_keys("ind")
       val =  self.verifyLinkPresence("#country")
       val.send_keys("ind")
       time.sleep(8)
       #checkOutPg.getDropDown().send_keys("ind")
       # countries = wait.until(
       #     expected_conditions.presence_of_all_elements_located(checkOutPg.getCountries()))
       # for country in countries:
       #     print(country.text)
       #     if country.text == "India":
       #         country.click()
       #         break
       #
       # wait.until(expected_conditions.element_to_be_clickable(
       #     (checkOutPg.getCheckbox()))).click()
       # wait.until(expected_conditions.element_to_be_clickable(checkOutPg.getPurchase())).click()
       # successMsg = wait.until(expected_conditions.visibility_of_element_located(checkOutPg.getSuccessMsg())).text
       #
       # print(successMsg)
       # assert "Success" in successMsg


