from selenium import webdriver
import time
import platform

executable = ''

if platform.system() == 'Windows':
    print('Detected OS : Windows')
    executable = './chromedriver/chromedriver_win.exe'
elif platform.system() == 'Linux':
    print('Detected OS : Linux')
    executable = './chromedriver/chromedriver_linux'
elif platform.system() == 'Darwin':
    print('Detected OS : Mac')
    executable = './chromedriver/chromedriver_mac'
else:
    assert False, 'Unknown OS Type'

# browser = webdriver.Chrome(executable)
