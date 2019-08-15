# need to install pip install pytest-ordering
import pytest

@pytest.fixture()
def setup():
	print("Once before every method")

@pytest.mark.run(order=2)
def test_methodA(setup):
	print("Running Method A")

@pytest.mark.run(order=1)
def test_methodB(setup):
	print("Running Method B")

