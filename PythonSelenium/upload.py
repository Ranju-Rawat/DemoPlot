from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

servObj = Service("\\Users\\rawat\\Downloads\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=servObj)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/upload-download-test/index.html")

driver.find_element(By.ID, "downloadButton").click()

# edit the excel with updated value
file_input = driver.find_element(By.XPATH, "//input[@type='file']")
file_input.send_keys("C:\\Users\\rawat\\Downloads\\download.xlsx")
wait = WebDriverWait(driver, 5)
#toastMsg = wait.until(expected_conditions.visibility_of_element_located(By.XPATH, "//div[contains(text(),'Updated Excel Data Successfully.')]"))
toastMsg = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Updated Excel Data Successfully.')]")))

print(toastMsg.text)