from selenium import webdriver
import time

driver = webdriver.Edge()
driver.get("https://developer.mozilla.org/en-US/docs/Learn")
print(driver.name)
print(driver.title)
print(driver.current_url)
print(driver.capabilities)
print(driver.capabilities['browserVersion'])
driver.find_element_by_link_text('Introduction to HTML').click()
driver.quit()