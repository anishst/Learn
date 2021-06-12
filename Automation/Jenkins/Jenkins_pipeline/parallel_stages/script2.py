import time

from selenium import webdriver
driver = webdriver.Edge()
driver.get("http://www.python.org")
time.sleep(3)
driver.quit()
 