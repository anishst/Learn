import time

from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://www.google.com")
print(driver.title)
time.sleep(2)
assert False
driver.quit()
 