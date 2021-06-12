import pytest, os
from selenium import webdriver

driver = None

test_env_var = os.getenv('flask_dev')
user_id = os.getenv('HLAS_USR')
user_pwd = os.getenv('HLAS_PSW')

@pytest.yield_fixture()
def setup():
    print("Once before every method")
    global driver
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
    print("Once after every method")

def test_methodA(setup):
    print("Running Method A")
    driver.get("http://www.google.com")
    print(test_env_var)
    if user_id:
        print(f"user id: {user_id}")
        print(f"user pwd {user_pwd}")
    else:
        print("No jenkins var found")
