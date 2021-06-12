from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# cap = DesiredCapabilities().FIREFOX
# cap["marionette"] = False
# browser = webdriver.Firefox(capabilities=cap,firefox_binary="C:\\Python\\selenium\\webdriver\\geckodriver.exe")
# browser.get('http://google.com/')
# browser.quit()

browser = webdriver.Firefox()
browser.get('http://google.com/')
browser.quit()