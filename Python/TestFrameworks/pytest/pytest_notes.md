# PyTest

Pytest is a testing framework which allows us to write test codes using python. This can be selenium scripts, api tests, DB tests etc.

## Install
Install: ```pip install pytest```

Check Version: ```pytest --version```

## Pytest Fixture Scopes

- function	Run once per test (default)
- class	Run once per class of tests
- module	Run once per module 
- session	Run once per session

## conftest.py

conftest.py is a special named file that pytest looks for when running tests.

## Running tests from Command Line

| Command | Description |
| -------- | -------- |
| ```pytest -v ---s```| enable verbose and show console msgs|
|```pytest --collect-only --quiet```| get list of tests; don't run|
|```pytest --collect-only -qq```|When used twice (or more), --quiet will print the amount of tests per module:|
|```pytest <modulename>.py```| run tests in module|
|```pyest somepath``` | run all tests below somepath|
|```pyest -k creditCards ``` | run all tests with name(keyword) creditCards|
|```ptest test_module.py::test_method``` | run certain method|
|```pytest -v -m cardtests```| runs tests with 'cardtests' as marker|
| ```pytest pytest-example.py --driver Chrome --html=report.html```| Example Code to run a test and output results to html format; note you need to install ```pytest-html``` package for this to work|
|```pytest pytest-otcnet.py --driver=Ie -v```| Show more details using -v flag
| ```pytest pytest-otcnet.py -k Demo --driver=Ie -v``` | Running tests with  certain name by providing the -k flag and then keyword; example below runs test case fucntions with 'Demo' in the name: |
|```pytest pytest_example_custom_markers.py -m mac -v``` | Skip tests by using custom marker tags by providing -m flag following by flagname; example runs test tagged with 'mac' flagname. To use negation: ```pytest pytest_example_custom_markers.py -m "not mac"  -v```|
|```pytest -rfp```| shows all passed failed tests|
| ```pytest -v --result-log=test.txt```| pipe run results to a file|
| ```pytest --junitxml='results.xml' ```| generate junit xml file; this can be used with Jenkins; shell command: ```pytest --junitxml='BUILD_$(BUILD_NUMBER)_results.xml``` then create a post-buid action to generate rpt using xml file; https://bah.udemy.com/course/elegant-automation-frameworks-with-python-and-pytest/learn/lecture/10176262?start=480#overview |

## Using Fixtures
| Fixture Usage | Description |
| -------- | -------- |
| ``` @pytest.mark.skip(reason='Skipping due to defect')``` |Skipping  a test |
| ```@pytest.mark.run(order=2)```| Set order of test execution; need to install pytest-ordering : ```pip install pytest-ordering``` https://pytest-ordering.readthedocs.io/en/develop/|
|```@pytest.mark.skipif(sys.version_info < (3,5)reason='Skipping due to defect')``` | Skipping  a test based on a condition|
| ```    @pytest.mark.parametrize("param_var_name", ['param1',                       'param2',                                 'param3'])```| Parameter fixture - single parameter |
|```@pytest.mark.parametrize("msg_number,display_number, msg_title, msg_content", [(0, 1, 'Test Msg1', 'Test Msg Content 1'),(3, 4, 'Test Msg4', 'Test Msg Content 4')])```|multiple parameters|
|```@pytest.mark.usefixtures("one_time_setups")class TestStability():```| Class level fixture |



## Running Tests in Parallel

https://pypi.org/project/pytest-xdist/#description

https://github.com/pytest-dev/pytest-xdist

```
install xdist: pip install -U pytest-xdist
py.test -n
```

## Reporting with Allure

https://docs.qameta.io/allure/#_pytest

Manual Install for Windows: https://docs.qameta.io/allure/#_manual_installation

## Known Issues
- Issue#1: upgrading to pytest version above 4.0.2 causes issues

## Resources
- PyTest Docs: https://docs.pytest.org/en/latest/getting-started.html
- PyTest-Selenium: https://pytest-selenium.readthedocs.io/en/latest/index.html
- Reporting with Pytest usign Allure Framework: https://docs.qameta.io/allure/#_pytest
- Fixtures: https://docs.pytest.org/en/latest/fixture.html
- pytest guide: https://www.lambdatest.com/blog/test-automation-using-pytest-and-selenium-webdriver/
- pytest in PyCharm: https://www.jetbrains.com/help/pycharm/pytest.html
- ChangeLog: https://docs.pytest.org/en/latest/changelog.html
- http://pythontesting.net/framework/pytest/pytest-fixtures-easy-example/
- coverage - https://coverage.readthedocs.io/en/v4.5.x/index.html
- https://www.blazemeter.com/blog/improve-your-selenium-webdriver-tests-with-pytest
- cheat sheet: https://gist.github.com/kwmiebach/3fd49612ef7a52b5ce3a

## Videos
- https://www.youtube.com/watch?v=8mp_1Jt-xHQ&t=931s