# https://realpython.com/modern-web-automation-with-python-and-selenium/

from selenium import webdriver  
from selenium.webdriver.firefox.options import Options 

headless_driver = True

if headless_driver == True:
	opts = Options()
	opts.set_headless()
	assert opts.headless # verify operatiing in headless mode	
	driver = webdriver.Firefox(options=opts) 
else:
	driver = webdriver.Firefox()
print("Navigating to Google")
driver.get("http://www.google.com")
driver.find_element_by_name('q').send_keys("test")
driver.quit()
print("Test Finished")