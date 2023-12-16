from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)

driver = webdriver.Chrome()
driver.get('https://www.python.org/')

event_time = driver.find_elements(By.CSS_SELECTOR,value='.event-widget time')
event_name = driver.find_elements(By.CSS_SELECTOR,value='.event-widget li a')
events = {}

for n in range(len(event_time)):
    events[n] ={
        "time": event_time[n].text,
        "name": event_name[n].text,
    }

print(events)
driver.quit() 