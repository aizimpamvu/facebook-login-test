# This is a sample Python script.
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


driver.get("https://www.facebook.com/")

email =driver.find_element(By.ID, "email")
email.send_keys("hallyizza200@gmail.com")

