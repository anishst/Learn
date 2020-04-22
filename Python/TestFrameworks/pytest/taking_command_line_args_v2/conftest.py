# content of conftest.py
import pytest


def pytest_addoption(parser):
    parser.addoption("--setup", action="store", help="setup.")
    parser.addoption("--browser", action="store", help="browser.")


@pytest.fixture
def setup_option(request):
    return request.config.getoption("--setup")

@pytest.fixture
def setup_option2(request):
    return request.config.getoption("--browser")

