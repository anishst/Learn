import  pytest

@pytest.yield_fixture()
def setup():
	print("Running Method level setup")
	yield
	print("Running Method level tearDown")


@pytest.yield_fixture(scope="module")
def oneTimeSetup():
	print("Running one time setup")
	yield
	print("Running one time tearDown")