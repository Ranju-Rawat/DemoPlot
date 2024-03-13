import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="class")
def preSetup(request):
    objServ = Service("C:\\Users\\rawat\\Downloads\\chromedriver-win64\\chromedriver.exe")
    driver = webdriver.Chrome(service=objServ)
    driver.get("https://main.d7wjioi25vh3e.amplifyapp.com/")
    request.cls.driver = driver
    yield
    driver.close()