from selenium import webdriver
from selenium.webdriver.common.by import By

#To keep the chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome()
driver.get("https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")

price_dollar = driver.find_element(By.CLASS_NAME,value='a-price-whole').text
price_cents = driver.find_element(By.CLASS_NAME,value='a-price-fraction').text

print(f"The price is {price_dollar}.{price_cents}")

# driver.close() # only closes the active tab
# driver.quit() # quits the entire program