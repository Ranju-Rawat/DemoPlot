import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="testing"
    )

@pytest.fixture(scope="class")
def setup(request):
    servObj = None
    browser_nm = request.config.getoption("browser_name")
    if browser_nm == "chrome":
        servObj = Service("\\Users\\rawat\\Downloads\\chromedriver-win64\\chromedriver.exe")
    else:
        print("Browser is not chrome")
    driver = webdriver.Chrome(service=servObj)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver
    yield
    driver.close()


