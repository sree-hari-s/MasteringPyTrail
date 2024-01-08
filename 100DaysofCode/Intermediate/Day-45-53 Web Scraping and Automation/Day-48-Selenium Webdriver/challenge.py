"""
Automate to sign up this form
https://secure-retreat-92358.herokuapp.com/ 
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=chrome_options)

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
email_address = input("Enter your email address: ")

driver.get('https://secure-retreat-92358.herokuapp.com/')
fname = driver.find_element(By.NAME,value='fName')
fname.send_keys(f'{first_name}')
lname = driver.find_element(By.NAME,value='lName')
lname.send_keys(f'{last_name}')
email = driver.find_element(By.NAME,value='email')
email.send_keys(f'{email_address}')
submit = driver.find_element(By.CLASS_NAME,value='btn')
submit.send_keys(Keys.ENTER)

time.sleep(2)
driver.quit()