# This is a sample Python script.
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

EMAIL = "hallyizza200@gmail.com"
PASS = "123454321"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.facebook.com/")

# Get and set email
email = driver.find_element(By.ID, "email")
time.sleep(3)
email.send_keys(EMAIL)
time.sleep(3)

# Get and set password

password = driver.find_element(By.ID, "pass")
password.send_keys(PASS)

time.sleep(3)

password.send_keys(Keys.ENTER)
# login = driver.find_element(By.TAG_NAME, 'button')
# print(login.text)
# login.click()

time.sleep(3)


driver.quit()