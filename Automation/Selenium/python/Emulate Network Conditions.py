# https://www.lambdatest.com/blog/selenium-with-python/
# Emulate Network Conditions
# https://github.com/SeleniumHQ/selenium/blob/474d11671452ffc6830e3b9603d6e438c9cce8fd/py/selenium/webdriver/chromium/webdriver.py
import pytest
from selenium import webdriver
import sys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from time import sleep
import urllib3
import warnings
# need selenum 4te
from selenium.webdriver.support.relative_locator import with_tag_name
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
import json
def test_emulate_network_settings():
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        web_driver = webdriver.Chrome(options=chrome_options)
        web_driver.maximize_window()
        time.sleep(2)
        web_driver.set_network_conditions(
                    offline = False,
                    latency = 10,
                    download_throughput = 500 * 1024,
                    upload_throughput = 500 * 1024)
        web_driver.get('https://www.lambdatest.com')
        net_con = web_driver.get_network_conditions()
        print()
        print(net_con)
        time.sleep(5)
        print("Latency: " + str(net_con["latency"]))
        print("Download Throughput: " + str(net_con['download_throughput']))
        print("Upload Throughput: " + str(net_con['upload_throughput']))
        print()
        # Release resources held by the Selenium WebDriver
        web_driver.quit()
        print("Emulation of Network Settings Test is complete")
