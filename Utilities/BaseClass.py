import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service



@pytest.mark.usefixtures("preSetup")
class BaseClass:
    pass

