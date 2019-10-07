# https://pytest-ordering.readthedocs.io/en/develop/
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


@pytest.mark.second_to_last
def test_three():
    assert True

@pytest.mark.last
def test_four():
    assert True

@pytest.mark.second
def test_two():
    assert True

@pytest.mark.first
def test_one():
    assert True


# relative to other tests
@pytest.mark.run(after='test_second')
def test_third():
    assert True

def test_second():
    assert True

@pytest.mark.run(before='test_second')
def test_first():
    assert True