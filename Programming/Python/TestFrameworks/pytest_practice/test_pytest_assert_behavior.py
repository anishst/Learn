# http://pythontesting.net/framework/pytest/pytest-fixtures-nuts-bolts/#bare
import pytest

@pytest.fixture()
def before():
    print('\nbefore each test')
 
def test_1(before):
    print('test_1()')
    assert False
 
def test_2(before):
    print('test_'
          '2()')