import pytest
# https://bah.udemy.com/course/learn-selenium-automation-in-easy-python-language/learn/lecture/16925040?start=510#overview

@pytest.mark.usefixtures("setup")
@pytest.mark.usefixtures("cross_browser")
@pytest.mark.usefixtures("cross_browser_three_values")
class TestCrossBrowser():

	# runs 2 times
	def test_selenium_method(self, cross_browser):
		print(cross_browser)


	def test_selenium_method_3_values(self, cross_browser_three_values):
		print(cross_browser_three_values)



