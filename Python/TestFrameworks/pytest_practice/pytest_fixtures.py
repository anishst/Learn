import pytest

@pytest.fixture()
def setup():
	print("Once before every method")


def test_methodA(setup):
	print("Running Method A")

def test_methodB(setup):
	print("Running Method B")

