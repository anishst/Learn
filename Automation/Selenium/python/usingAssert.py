#https://www.w3schools.com/xml/xpath_syntax.asp

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.google.com")

assert "Google" in driver.title
assert "Gmail" in driver.page_source
assert driver.find_element_by_link_text("Gmail")

driver.quit()