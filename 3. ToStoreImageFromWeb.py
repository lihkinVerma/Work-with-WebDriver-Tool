
# importing required libraries
import urllib
from selenium import webdriver

# connecting to browser
driver = webdriver.Chrome()
driver.get('https://www.alexa.com/siteinfo/alexa.com')

# get the image source
img = driver.find_element_by_xpath('//section[@id="traffic-rank-content"]/div/span[2]/div[1]/span/span/div/img')
src = img.get_attribute('src')

# download the image
urllib.urlretrieve(src, "captcha.png")

driver.close()