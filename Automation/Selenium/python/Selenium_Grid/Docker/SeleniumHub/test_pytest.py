from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

chrome = webdriver.Remote(
          command_executor='http://localhost:4444/wd/hub',
          desired_capabilities=DesiredCapabilities.CHROME)
firefox = webdriver.Remote(
          command_executor='http://localhost:4444/wd/hub',
          desired_capabilities=DesiredCapabilities.FIREFOX) 

def test_test1():
	print("testing chrome using Docker image")
	chrome.get('https://www.google.com')
	print(chrome.title)

def test_test2():
	print("testing chrome using Docker image")
	chrome.get('https://www.google.com')
	print(chrome.title)

def test_fftest1():	
	print("Testing firefox using Docker Image")
	firefox.get('https://www.google.com')
	print(firefox.title)


def test_fftest2():	
	print("Testing firefox using Docker Image")
	firefox.get('https://www.google.com')
	print(firefox.title)

# chrome.quit()
# firefox.quit()