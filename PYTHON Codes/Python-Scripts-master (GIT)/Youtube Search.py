from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Firefox()
driver.get("http://youtube.com")

search=input("What to search in youtube: ")

try:
	ytbSearch=driver.find_element_by_id("masthead-search-term")
	ytbSearch.send_keys(str(search))
	
	vidSearch=driver.find_element_by_id("search-btn")
	vidSearch.click()
	
	time.sleep(7)
finally:
	pass
