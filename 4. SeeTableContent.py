
# importing required libraries
import urllib
from selenium import webdriver

# connecting to browser
driver = webdriver.Chrome()
driver.get('https://www.alexa.com/siteinfo/alexa.com')

# finding the table
table_id = driver.find_element_by_id('demographics_div_country_table')
rows = table_id.find_elements_by_tag_name("tr") 

# get all of the rows in the table
for row in rows:
	cells = row.find_elements_by_tag_name("td");
	for cell in cells:
		cell_content = cell.text;
		print(cell_content);
	
driver.close()
