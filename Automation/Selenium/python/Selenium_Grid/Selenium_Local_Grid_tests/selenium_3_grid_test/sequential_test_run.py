# https://testdriven.io/blog/distributed-testing-with-selenium-grid/
from subprocess import check_call
import sys
import subprocess
import os

for counter in range(1):
    os.environ['BROWSER'] = 'chrome'
    chrome_cmd = "python test.py"
    # os.environ['BROWSER'] = 'internet explorer'
    # ie_cmd = 'python test.py'
    check_call(chrome_cmd, shell=True)
    # check_call(ie_cmd, shell=True)