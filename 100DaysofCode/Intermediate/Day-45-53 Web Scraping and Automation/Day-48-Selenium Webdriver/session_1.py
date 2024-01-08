from selenium import webdriver

#To keep the chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome()
driver.get("https://www.amazon.in")

driver.close() # only closes the active tab
driver.quit() # quits the entire program