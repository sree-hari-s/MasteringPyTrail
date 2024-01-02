import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv

load_dotenv()

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = os.environ['TWITTER_EMAIL']
TWITTER_PASSWORD = os.environ['TWITTER_PASSWORD']
TWITTER_USERNAME = os.environ['TWITTER_USERNAME']
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

class InternetSpeedTwitterBot:
    def __init__(self,chrome_options):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.up = 30
        self.down = 30

    def get_internet_speed(self):
        speed_test_url = 'https://fast.com/'
        self.driver.get(url=speed_test_url)
        time.sleep(40)
        show_more_info = self.driver.find_element(By.ID,value='show-more-details-link')
        show_more_info.click()
        
        self.download_speed = self.driver.find_element(By.ID,value='speed-value').text
        time.sleep(25)
        self.upload_speed = self.driver.find_element(By.ID,value='upload-value').text
        print(f"Download Speed : {self.download_speed}\nUpload Speed : {self.upload_speed}")
        
    def twitter_login(self):
        self.driver.get("https://twitter.com/login")
        time.sleep(5)
        email = self.driver.find_element(By.XPATH,value='/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        email.send_keys(TWITTER_EMAIL)
        email.send_keys(Keys.ENTER)
        print("Email entered")
        time.sleep(2)
        username = self.driver.find_element(By.XPATH,value='/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        username.send_keys(TWITTER_USERNAME)
        print("Username entered")
        username.send_keys(Keys.ENTER)
        time.sleep(3)
        password = self.driver.find_element(By.XPATH,value='/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)
        print("Password entered")
        self.post_tweet()
    
    def post_tweet(self):
        time.sleep(5)
        tweet_input = self.driver.find_element(By.XPATH,value='/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        tweet = f"Hey @JioCare I am getting my download as {self.download_speed} Mbps and upload speed as {self.upload_speed} Mbps \n as what you promised from Rs 599 plan of download speed of {self.down} Mbps and upload speed  {self.up} Mbps."
        time.sleep(5)
        tweet_input.send_keys(tweet)
        post_button = self.driver.find_element(By.XPATH,value='/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div/span/span')
        post_button.click()
        print("Tweet posted successfully")
        
bot = InternetSpeedTwitterBot(chrome_options)
bot.get_internet_speed()
bot.twitter_login()