import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv

load_dotenv()

URL = "https://www.linkedin.com/jobs/search/?currentJobId=3789843167&f_AL=true&f_E=3&f_WT=2&keywords=python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

email = os.environ["EMAIL"]
password = os.environ["PASSWORD"]

driver.get(url=URL)
