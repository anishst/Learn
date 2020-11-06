# https://stackoverflow.com/questions/51009174/running-pytest-main-does-not-collect-tests
import time

import pytest

html_path = 'reports/report' + time.strftime("%d%m%Y_%H%M%S") +'.html'
junit_path = 'reports/junit'  + time.strftime("%d%m%Y_%H%M%S") + '.xml'
result_log_path = '.\Reports\/Logs\/Execution_' + time.strftime("%d%m%Y_%H%M%S") + '.log'
pytest_args = [
    '-v', # verbose mode
    '-s', # print statements
    '--html',
    html_path,
    '--junitxml',
    junit_path,
    '--resultlog',
    result_log_path,
    'test_module.py',
    'test_module2.py',
    'test_module2.py::TestFooBar'
]
pytest.main(pytest_args)