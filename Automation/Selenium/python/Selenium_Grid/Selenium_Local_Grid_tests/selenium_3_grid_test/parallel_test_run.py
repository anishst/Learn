# https://testdriven.io/blog/distributed-testing-with-selenium-grid/
from subprocess import Popen
import os

processes = []

for counter in range(10):
    os.environ['BROWSER'] = 'chrome'
    chrome_cmd = 'python test.py'
    processes.append(Popen(chrome_cmd, shell=True))
    # processes.append(Popen(firefox_cmd, shell=True))


for counter in range(10):
    processes[counter].wait()