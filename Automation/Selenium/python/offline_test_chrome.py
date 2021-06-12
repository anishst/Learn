# works 9/15/20
# https://github.com/SeleniumHQ/selenium/blob/trunk/py/test/selenium/webdriver/chrome/chrome_network_emulation_tests.py
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.set_network_conditions(offline=True, latency=5, throughput=500 * 1024)

try:

    driver.get("https://developer.mozilla.org/en-US/docs/Learn")
    driver.find_element_by_link_text('Introduction to HTML').click()
except:
    print("Browser is offline")

print("Turning internet back on...")
driver.set_network_conditions(offline=False, latency=5, throughput=500 * 1024)
driver.get("https://developer.mozilla.org/en-US/docs/Learn")
driver.find_element_by_link_text('Introduction to HTML').click()
driver.quit()