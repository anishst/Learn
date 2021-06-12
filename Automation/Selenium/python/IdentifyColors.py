from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")

cssValues = {'border', 'color', 'background-color'}

text = driver.find_element_by_class_name("gb_P")

for value in cssValues:
	print(value + ": " + text.value_of_css_property(value))

driver.quit()