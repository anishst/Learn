import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.mark.usefixtures(scope="module")
class TestGoogle():

    def test_SearchForCheese(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get('https://www.google.com/')
        print(driver.title)
        driver.save_screenshot('test.png')
        print("Script finished.")

    def test_SearchForPython(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get('https://www.python.org/')
        print(driver.title)
        driver.save_screenshot('test.png')
        print("Script finished.")




