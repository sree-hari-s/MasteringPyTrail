from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import sqrt

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID,"cookie")
cps_element = driver.find_element(By.ID,"cps")
initialize = time.time()
loop_start = initialize
increment = 3

while time.time() <= initialize + 300:
    cookie.click()
    if time.time() > loop_start + increment:
        loop_start = time.time()
        cps = float(cps_element.text.split()[2])
        increment = 3 + sqrt(cps)
        products = driver.find_elements(By.XPATH,"//div[@id='store']/div[not(@class='grayed')]")
        if len(products)>0:
            products[-1].click()