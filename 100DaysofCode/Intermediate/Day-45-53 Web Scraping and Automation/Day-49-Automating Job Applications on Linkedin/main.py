import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
from selenium.common.exceptions import NoSuchElementException

load_dotenv()

URL = "https://www.linkedin.com/jobs/search/?currentJobId=3789843167&f_AL=true&f_E=3&f_WT=2&keywords=python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

ACCOUNT_EMAIL = os.environ["EMAIL"]
ACCOUNT_PASSWORD = os.environ["PASSWORD"]

driver.get(url=URL)

# Click Sign in Button
try:
    time.sleep(2)
    sign_in_button = driver.find_element(by=By.LINK_TEXT, value="Sign in")
    sign_in_button.click()
except NoSuchElementException:
    print("No such element")

# Sign in
time.sleep(5)
email_field = driver.find_element(by=By.ID, value="username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(by=By.ID, value="password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

#Locate Save button
time.sleep(5)
save_button = driver.find_element(By.CSS_SELECTOR,value=".jobs-save-button")
save_button.click()

#Locate the apply button
time.sleep(5)
apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
apply_button.click()

#Submit the application
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
submit_button.click()