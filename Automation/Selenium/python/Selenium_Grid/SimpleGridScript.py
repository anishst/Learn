from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

driver = webdriver.Remote(
   command_executor='http://127.0.0.1:4444/wd/hub',
   desired_capabilities=DesiredCapabilities.CHROME)

driver.get("https://www.google.com/");
print (driver.session_id)

print (driver.title)
time.sleep(5)
driver.quit();