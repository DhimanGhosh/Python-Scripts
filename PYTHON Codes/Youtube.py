from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time

url = 'https://www.youtube.com/watch?v=KZsr_xOOGlQ'
refresh = 4
count = 3
browser = webdriver.Firefox()
main_window = browser.current_window_handle
    
for i in range(0, int(count)):
      browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
      browser.get(url)
      time.sleep(int(refresh))
      browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')
