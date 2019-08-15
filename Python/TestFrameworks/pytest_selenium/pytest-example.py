import pytest

def test_example(selenium):
    selenium.get('http://www.example.com')


def test_example2(selenium):
    selenium.get('http://www.example.com')


test_example(selenium)