import  pytest

@pytest.yield_fixture()
def setup():
	print("Running Method level setup")
	yield
	print("Running Method level tearDown")

@pytest.yield_fixture(scope="module")
def oneTimeSetup(browser,osType):
	print("Running one time setup")
	if browser == "Chrome":
		print("running tests on Chrome")
	else:
		print("Running on tests on Ie")
	yield
	print("Running one time tearDown")

def pytest_addoption(parser):
	parser.addoption("--browser", help="Type of browser")
	parser.addoption("--osType", help="Type of OS")

@pytest.fixture(scope="session")
def browser(request):
	return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
	return request.config.getoption("--osType")