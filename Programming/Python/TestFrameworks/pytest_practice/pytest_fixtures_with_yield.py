import pytest

@pytest.yield_fixture()
def setup():
	print("Once before every method")
	yield
	print("Once after every method")

def test_methodA(setup):
	print("Running Method A")

def test_methodB(setup):
	print("Running Method B")

