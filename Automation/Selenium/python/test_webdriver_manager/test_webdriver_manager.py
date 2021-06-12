# https://github.com/SergeyPirogov/webdriver_manager

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time

# CHROM
# by default it will use latest version
# driver = webdriver.Chrome(ChromeDriverManager().install())
# to use a specific version of driver use this
# driver = webdriver.Chrome(ChromeDriverManager('2.36').install())
#
# driver = webdriver.Ie(IEDriverManager(os_type='Win32').install()) # to download 32-bit version of IE
driver = webdriver.Ie(IEDriverManager().install()) # to download 64-bit version of IE
# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())


driver.get("http://google.com")
driver.find_element_by_name('q').send_keys('test')
time.sleep(5)
driver.close()
driver.quit()