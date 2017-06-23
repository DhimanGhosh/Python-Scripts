from selenium import webdriver
from selenium.webdriver.remote import switch_to

driver=webdriver.Firefox()

for i in range(0,10):
    driver.execute_script("window.open()")
    driver.switch_to_window(driver.window_handles[i+1])
