# http://pythontesting.net/framework/pytest/pytest-fixtures-nuts-bolts/#bare
import sys

import pytest

@pytest.fixture()
def before():
    print('\nbefore each test')

@pytest.mark.skipif(sys.platform == 'win32', reason='skipping on windows')
def test_1(before):
    print('test_1()')
 
def test_2(before):
    print('test_2()')