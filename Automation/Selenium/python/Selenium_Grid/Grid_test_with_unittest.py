import unittest #https://docs.python.org/3/library/unittest.html
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from selenium.webdriver.common.keys import Keys

class GoogleTestCase(unittest.TestCase): #Test suite name for grouping related test cases.

	@classmethod
	def setUpClass(cls):						#Optional test statements run before all test cases
		cls.driver = webdriver.Remote(
				   command_executor='http://127.0.0.1:4444/wd/hub',
				   desired_capabilities=DesiredCapabilities.INTERNETEXPLORER)
		cls.driver.implicitly_wait(10)
	@classmethod
	def tearDownClass(cls):						#Optional test statements run after all test cases
		cls.driver.quit()

	def setUp(self):							#Optional test statements run before each test case.
		self.driver.get("http://www.google.com")

	def tearDown(self):							#Optional test statements run after each test case.
		pass
		print("test")
		time.sleep(5)
		# self.driver.find_element_by_link_text("Sign off").click()

	def test_first_tc(self):					#Individual test case
		self.assertEqual("Google", self.driver.title)
		self.driver.find_element_by_name("q").send_keys("Python")
		self.driver.find_element_by_name("q").send_keys(Keys.RETURN)
		self.assertIn("Python", self.driver.find_element_by_partial_link_text("Python").text)

	def test_second_tc(self):					#Individual test case
		self.assertEqual("Google", self.driver.title)
		self.driver.find_element_by_name("q").send_keys("Google")
		self.driver.find_element_by_name("q").send_keys(Keys.RETURN)


	def test_third_tc(self):					#Individual test case
		self.assertEqual("Google", self.driver.title)
		self.driver.find_element_by_name("q").send_keys("Cheese")
		self.driver.find_element_by_name("q").send_keys(Keys.RETURN)


	def test_Fourth_tc(self):					#Individual test case
		self.assertEqual("Google", self.driver.title)
		self.driver.find_element_by_name("q").send_keys("Python")
		self.driver.find_element_by_name("q").send_keys(Keys.RETURN)
		self.assertIn("Python", self.driver.find_element_by_partial_link_text("Python").text)

if __name__ == '__main__':
    unittest.main(verbosity=2)