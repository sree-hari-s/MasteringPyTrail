from selenium import webdriver
from selenium.webdriver.common.by import By

#To keep the chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome()
driver.get("https://python.org/")

search_bar = driver.find_element(By.NAME,value='q')
print(search_bar.get_attribute('placeholder'))
button = driver.find_element(By.ID,value='submit')
print(button.size)
documentation_link = driver.find_element(By.CSS_SELECTOR,value='.documentation-widget a')
print(documentation_link.text)

bug_link = driver.find_element(By.XPATH,value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)


# driver.close() # only closes the active tab
# driver.quit() # quits the entire program