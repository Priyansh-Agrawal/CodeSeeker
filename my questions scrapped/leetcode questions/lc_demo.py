# import required packages

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup

# Define the chromedriver service
s = Service('chromedriver.exe')

# instantiate the webdriver
driver = webdriver.Chrome(service=s)

# the base url for the pages to scrape
page_url= "https://leetcode.com/problemset/all/?page=1"

# Function to get all the 'a' tags from a given URL
def get_a_tags(url):
    driver.get(url)
    time.sleep(7)
    links= driver.find_elements(By.TAG_NAME,"a")
    ans=[]
    pattern="/problems"
    
    
    for i in links:
        try:
            if pattern in i.get_attribute("href"):
                ans.append(i.get_attribute("href"))
        except:
            pass    
    print (ans)
get_a_tags(page_url)

time.sleep(5)

