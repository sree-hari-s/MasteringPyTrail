import os
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
from selenium.common.exceptions import ElementNotInteractableException

load_dotenv()

FORM_URL = 'https://docs.google.com/forms/d/e/1FAIpQLSdVG_MMTmZqsCSiePGJ-vt3rz9USIbYlqwEg93pKkaYwupAwg/viewform?usp=sf_link'

RENTAL_URL = 'https://appbrewery.github.io/Zillow-Clone/'

response = requests.get(RENTAL_URL)
soup = BeautifulSoup(response.text,'html.parser')

listing_names = []
listing_price = []
listing_links = []

titles = soup.find_all('address')
listing_names = [ad_name.getText().strip() for ad_name in titles]
#print(listing_names)

prices = soup.find_all('span',attrs={"data-test":"property-card-price"})
listing_price = [price.getText().strip('+ /mo').split("+")[0] for price in prices]
#print(listing_price)

ad_link = soup.find_all('a',class_='property-card-link')
listing_links = [ad['href'] for ad in ad_link]
#print(listing_links)

print(f"{len(listing_names)}\n{len(listing_price)}\n{len(listing_links)}")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=chrome_options)

try:
    for i in range(len(listing_names)):
        driver.get(url=FORM_URL)
        try:
            address_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'))
            )
            address_input.send_keys(listing_names[i])
            price_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'))
                )
            price_input.send_keys(listing_price[i])
            link_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'))
                )
            link_input.send_keys(listing_links[i])    
            submit_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span'))
                )
            submit_button.click()
        except ElementNotInteractableException:
            driver.refresh()
            continue
finally:
    driver.quit()