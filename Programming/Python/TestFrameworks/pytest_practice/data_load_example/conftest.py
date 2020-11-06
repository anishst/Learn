import  pytest

@pytest.yield_fixture(scope="class")
def setup():
	print("Run before all test")
	yield
	print("Run after all tests")

@pytest.fixture()
def data_load():
	print("Data for tests are created...")
	return ["Anish", "Sebastian", "pytester"]

@pytest.fixture(params=['chrome', 'ie'])
def cross_browser(request):
	return request.param

@pytest.fixture(params=[('chrome','anish','pwd'), ('ie','anish','pwd'), "IE"])
def cross_browser_three_values(request):
	return request.param
