import pytest

@pytest.mark.windows
def test_windows():
	assert True

@pytest.mark.windows
def test_windows2():
	assert True

@pytest.mark.mac
def test_mac1():
	assert True

@pytest.mark.mac
def test_mac2():
	assert True		