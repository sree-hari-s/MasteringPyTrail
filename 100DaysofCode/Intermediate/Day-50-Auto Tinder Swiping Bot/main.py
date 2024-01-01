import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from dotenv import load_dotenv

load_dotenv()

# FB credentials
EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]

URL = 'https://tinder.com/'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(url=URL)

login_button = driver.find_element(By.XPATH,value='/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
login_button.click()
print("Login Button Clicked")
time.sleep(2)

more_options = driver.find_element(By.XPATH,value='/html/body/div[2]/main/div[1]/div/div[1]/div/div/div[2]/div[2]/span/button')
more_options.click()
print("More Options Clicked")
time.sleep(2)

fb_login = driver.find_element(By.XPATH,value='//*[@id="u647161393"]/main/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div/div')
fb_login.click()
print("Fb login Started")

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

#Login and hit enter
email = driver.find_element(By.ID,value='email')
password = driver.find_element(By.ID,value='pass')
email.send_keys(EMAIL)
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)
print(driver.title)
print("Facebook Login Successfull")
time.sleep(5)

#Allow cookies 
cookies = driver.find_element(By.XPATH,value='/html/body/div[2]/main/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]')
cookies.click()
print("Cookies Accepted")

#Allow Location
allow_location = driver.find_element(By.XPATH,value='/html/body/div[2]/main/div/div/div/div[3]/button[1]/div[2]/div[2]')
allow_location.click()
print("Location service accepted")

#Disable notifications
notification_button = driver.find_element(By.XPATH,value='/html/body/div[2]/main/div/div/div/div[3]/button[2]/div[2]/div[2]')
notification_button.click()
print("Notifications disabled")


for n in range(25):

    #Add a 1 second delay between likes.
    time.sleep(2)

    try:
        print("called")
        like_button = driver.find_element(By.XPATH,
            '/html/body/div[1]/div/div[1]/div/div/main/div/div/div[1]/div/div[3]/div/div[4]/button')
        like_button.click()

    #Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR,".itsAMatch a")
            match_popup.click()

        #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            time.sleep(2)

driver.quit()