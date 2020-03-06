# https://docs.pytest.org/en/latest/reference.html#pytest-mark-parametrize
import pytest

@pytest.mark.parametrize('i', range(10))
def test_random(i):
	print("Hello world!")