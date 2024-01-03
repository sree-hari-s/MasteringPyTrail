import os
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
from selenium.common.exceptions import ElementClickInterceptedException

load_dotenv()

USERNAME=os.environ['INSTA_USERNAME']
PASSWORD=os.environ['INSTA_PASSWORD']
SIMILAR_ACCOUNT=os.environ['SIMILAR_ACCOUNT']



class InstaFollower:
    def __init__(self):
        self.base_url = 'https://www.instagram.com'
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        
    def login(self):
        self.driver.get(self.base_url)
        time.sleep(2)
        username = self.driver.find_element(By.XPATH,value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input')
        username.send_keys(USERNAME)
        password = self.driver.find_element(By.XPATH,value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input')
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(4)
        # Dont save login info
        login_info = self.driver.find_element(By.XPATH,value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div')
        if login_info:
            login_info.click()
        time.sleep(4)
        # Dont send notifications
        notifications = self.driver.find_element(By.XPATH,value='/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
        if notifications:
            notifications.click()

    def find_followers(self):
        follower_url = f'{self.base_url}/{os.environ["SIMILAR_ACCOUNT"]}/followers/'
        self.driver.get(follower_url)
        time.sleep(5)        
        # TODO: scroll through the followers list
        close_button = self.driver.find_element(By.XPATH,value='/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/button').click()
        
    def follow(self):
        # Follow all the users followers.
        pass
    
    def logout(self):
        more_button = self.driver.find_element(By.XPATH,value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[3]/span/div/a/div')
        more_button.click()
        time.sleep(3)
        logout_button = self.driver.find_element(By.XPATH,value='/html/body/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div[1]/div/div[6]/div[1]')
        logout_button.click()
        self.driver.quit()

bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
bot.logout()