from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://developer.mozilla.org/en-US/docs/Learn")
driver.find_element_by_link_text('Introduction to HTML').click()
driver.back()
driver.refresh()
driver.forward()
time.sleep(3)

# driver.quit()