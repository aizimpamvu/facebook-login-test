# # This is a sample Python script.
# from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
# import time
#
# EMAIL = "hallyizza200@gmail.com"
# PASS = "123454321"
#
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# driver.get("https://www.facebook.com/")
#
# # Get and set email
# email = driver.find_element(By.ID, "email")
# time.sleep(3)
# email.send_keys(EMAIL)
# time.sleep(3)
#
# # Get and set password
#
# password = driver.find_element(By.ID, "pass")
# password.send_keys(PASS)
#
# time.sleep(3)
#
# password.send_keys(Keys.ENTER)
# # login = driver.find_element(By.TAG_NAME, 'button')
# # print(login.text)
# # login.click()
#
# time.sleep(3)
#
#
# driver.quit()
#

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep

FB_EMAIL = "hallyiizza200@gmail.com"
FB_PASSWORD = "Hally1234%"

# chrome_driver_path = "F:/udemy/chromedriver"
# driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("http://www.tinder.com")

sleep(2)
login_button = driver.find_element(By.XPATH,'//*[@id="q-1380955487"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
login_button.click()

sleep(2)
fb_login = driver.find_element(By.XPATH, '//*[@id="q1185630733"]/main/div/div[1]/div/div/div[3]/span/div[2]/button/div[2]/div[2]')
fb_login.click()

sleep(3)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

email = driver.find_element(By.XPATH,'//*[@id="email"]')
password = driver.find_element(By.XPATH,'//*[@id="pass"]')

email.send_keys(FB_EMAIL)
password.send_keys(FB_PASSWORD)
password.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)
print(driver.title)

sleep(5)
allow_location_button = driver.find_element(By.XPATH,'//*[@id="q-1380955487"]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]')
allow_location_button.click()
notifications_button = driver.find_element(By.XPATH,'//*[@id="mount_0_0_Q0"]/div/div/div/div/div/div/div/div[1]/div[3]/div[2]/div[1]/div/div/div')
notifications_button.click()
cookies = driver.find_element(By.XPATH,'//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

for n in range(100):
    sleep(1)
    try:
        print("called")
        like_button = driver.find_element(By.XPATH,
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            sleep(2)

driver.quit()