# Not working 9/15/20

from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions

edge_options = EdgeOptions()
# edge_options.page_load_strategy = 'normal'
edge_options.networkConnectionEnabled = True
driver = webdriver.Edge(capabilities=edge_options.to_capabilities())
# Navigate to url
driver.get("http://www.google.com")
# driver.quit()

# 'networkConnectionEnabled'
try:



    driver.get("https://developer.mozilla.org/en-US/docs/Learn")
    driver.find_element_by_link_text('Introduction to HTML').click()
except:
    print("Browser is offline")

print("Turning internet back on...")
# driver.set_network_conditions(offline=False, latency=5, throughput=500 * 1024)
driver.get("https://developer.mozilla.org/en-US/docs/Learn")
driver.find_element_by_link_text('Introduction to HTML').click()
driver.quit()