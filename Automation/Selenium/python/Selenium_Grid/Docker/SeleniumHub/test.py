from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

chrome = webdriver.Remote(
          command_executor='http://localhost:4444/wd/hub',
          desired_capabilities=DesiredCapabilities.CHROME)
firefox = webdriver.Remote(
          command_executor='http://localhost:4444/wd/hub',
          desired_capabilities=DesiredCapabilities.FIREFOX) 

print("testing chrome using Docker image")
chrome.get('https://www.google.com')
print(chrome.title)

print("Testing firefox using Docker Image")
firefox.get('https://www.google.com')
print(firefox.title)

chrome.quit()
firefox.quit()