from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Optional - Keep the browser open (helps diagnose issues if the script crashes)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

# Get cookie to click on.
cookie = driver.find_element(by=By.ID, value="cookie")

time_out = time.time() + 5
five_minute = time.time() + 60 * 5

while True:
    cookie.click()

    while time.time() > time_out:
        store_products = driver.find_elements(
            by="xpath", value='//*[@id="store"]/div[not(@class="grayed")]'
        )
        if len(store_products) > 0:
            store_products[-1].click()
            time_out = time_out + 5

    if time.time() > five_minute:
        cookie_per_s = driver.find_element(by="id", value="cps").text
        print(cookie_per_s)
        break

driver.close()
