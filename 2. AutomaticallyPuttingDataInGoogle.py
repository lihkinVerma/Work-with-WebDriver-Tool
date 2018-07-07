
# importing required libraries
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# making connection to browser
browser =webdriver.Chrome();
browser.get('http://www.google.com')

# acessing the search box
search = browser.find_element_by_name('q')

# writing content to search box
search.send_keys("google search through python")

# hit return after you enter search text
search.send_keys(Keys.RETURN)
time.sleep(5) # sleep for 5 seconds so you can see the results

# shutting the browser
browser.quit()