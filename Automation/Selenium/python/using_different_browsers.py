from selenium import webdriver
import time

def DriverList(browser):
    if browser.lower() == "ff" or browser.lower() == 'firefox':
        return webdriver.Firefox()    
    elif  browser.lower() == "ie":
        return webdriver.Ie()
    elif browser.lower() == "chrome":
        return webdriver.Chrome()
    elif browser.lower() == 'edge':
    	return webdriver.Edge()

browserList = ['edge']

for browser in browserList:

	driver = DriverList(browser)
	driver.get("https://www.google.com")

	#  find links by tag name
	elements = driver.find_elements_by_tag_name('a')
	for element in elements:
		print(element.text)

time.sleep(30)
driver.quit()