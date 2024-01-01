import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv

load_dotenv()

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = os.environ['TWITTER_EMAIL']
TWITTER_PASSWORD = os.environ['TWITTER_PASSWORD']
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

class InternetSpeedTwitterBot:
    def __init__(self,chrome_options):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        speed_test_url = 'https://fast.com/'
        self.driver.get(url=speed_test_url)
        time.sleep(40)
        show_more_info = self.driver.find_element(By.ID,value='show-more-details-link')
        show_more_info.click()
        
        download_speed = self.driver.find_element(By.ID,value='speed-value')
        time.sleep(40)
        upload_speed = self.driver.find_element(By.ID,value='upload-value')
        print(f"Download Speed : {download_speed.text}\nUpload Speed : {upload_speed.text}")
        
    def tweet_at_provider(self):
        pass


bot = InternetSpeedTwitterBot(chrome_options)
bot.get_internet_speed()
bot.tweet_at_provider()