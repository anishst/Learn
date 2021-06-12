from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC  # available since 2.26
from selenium.webdriver.common.keys import Keys
import time

def ExplicitWaitSimple(myDynamicElement):
		element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, myDynamicElement)))
		return element

"""This function takes in 2 args """
def FindElementandClick(how, what):
	if how == 'name':
		try:
			element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, what)))
			element.click()
		except:
			print("could not locate {} element with a value of: '{}'".format(how,what))
	elif how == 'link':
		try:
			element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, what)))
			element.click()
		except:
			print("could not locate {} element with a value of: '{}'".format(how,what))
	elif how == 'xpath':
		try:
			element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, what)))
			element.click()
		except:
			print("could not locate {} element with a value of: '{}'".format(how,what))	
	elif how == 'partialLink':
		try:
			element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT	, what)))
			element.click()
		except:
			print("could not locate {} element with a value of: '{}'".format(how,what))		
	elif how == 'css':
		try:
			element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, what)))
			element.click()
		except:
			print("could not locate {} element with a value of: '{}'".format(how,what))			
	else:
		try:
			element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.TAG_NAME, what)))
			element.click()
		except:
			print("could not locate {} element with a value of: '{}'".format(how,what))

		
		


driver = webdriver.Chrome()
driver.get("http://www.google.com")
elm = ExplicitWaitSimple('q')
elm.send_keys('python')
elm.send_keys(Keys.RETURN)
FindElementandClick('partialLink', 'Welcome to Python.org')
time.sleep(5)
driver.quit()




