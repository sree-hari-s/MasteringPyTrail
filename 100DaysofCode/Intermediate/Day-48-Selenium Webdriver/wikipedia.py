from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://en.wikipedia.org/wiki/Main_Page')


"""
article_count = driver.find_element(By.ID,value='articlecount')
print(article_count.text.split(" ")[0])
"""
# Alternative code
article_count = driver.find_element(By.CSS_SELECTOR,value='#articlecount a')
print(article_count.text)

# find the anchor tag and click it
encyclopedia = driver.find_element(By.LINK_TEXT,value='encyclopedia')
encyclopedia.click()

search = driver.find_element(By.NAME,'search')
# search.send_keys('Python'+Keys.ENTER)
search.send_keys(["Python", Keys.ENTER])