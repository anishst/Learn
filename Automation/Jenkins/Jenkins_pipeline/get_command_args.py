import sys, os
import time

# print( 'Number of arguments:', len(sys.argv), 'arguments.')
# print( 'Argument List:', str(sys.argv))
# print(os.getenv('USER_ID'))
# print(os.getenv('PSWD'))

from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("https://qae.otcnet.fms.treas.gov/")
driver.find_element_by_name('username').send_keys(os.getenv('USER_ID'))
driver.find_element_by_name('PASSWORD').send_keys(os.getenv('PSWD'))
driver.find_element_by_xpath("//input[@value='Log In']").click()
time.sleep(5)