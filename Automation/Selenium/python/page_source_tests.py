# https://www.lambdatest.com/blog/how-to-get-page-source-in-selenium-webdriver/
import time

from selenium import webdriver

# Get HTML Page source Using driver.page_source
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://pynishant.github.io/")
# pageSource = driver.page_source
# fileToWrite = open("page_source.html", "w")
# fileToWrite.write(pageSource)
# fileToWrite.close()
# fileToRead = open("page_source.html", "r")
# print(fileToRead.read())
# fileToRead.close()

# Get HTML Page Source Using driver.execute_javascript - eturns the innerHTML of the body element
print("*"*200)
pageSource = driver.execute_script("return document.body.innerHTML;")
print(pageSource)

# get outerthml
print("*"*200)
pageSource = driver.execute_script("return document.documentElement.outerHTML;")
print(pageSource)


# Get HTML Page Source In Selenium Python WebDriver Using XPath
pageSource = driver.find_element_by_xpath("//*").get_attribute("outerHTML")

# How To Retrieve HTML Source Of WebElement In Selenium?
elementSource = driver.find_element_by_id("div1").get_attribute("outerHTML")
print(elementSource)

# How To Get Page Source As XML In Selenium WebDriver?
# driver.execute_script('return document.getElementById(“webkit-xml-viewer-source-xml”).innerHTML')
# time.sleep(3)

# Get HTML Page Source Using “view-source:” URL
print("*"*200)
driver.get("view-source:https://pynishant.github.io/")


driver.quit()


# get page source using requests

# import requests
# url = 'https://pynishant.github.io/'
# pythonResponse = requests.get(url)
# fileToWrite = open("py_source.html", "w")
# fileToWrite.write(pythonResponse.text)
# fileToWrite.close()
# fileToRead = open("py_source.html", "r")
# print(fileToRead.read())
# fileToRead.close()

