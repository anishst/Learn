import  pytest

#  store results
def pytest_sessionstart(session):
    session.results = dict()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == 'call':
        item.session.results[item] = result


@pytest.yield_fixture()
def setup():
	print("Running Method level setup")
	yield
	print("Running Method level tearDown")


@pytest.yield_fixture(scope="module")
def oneTimeSetup():
	print("Running one time setup")
	yield
	print("Running one time tearDown")


#  get results and report 
def pytest_sessionfinish(session, exitstatus):
	print()
	print('run status code:', exitstatus)
	passed_amount = sum(1 for result in session.results.values() if result.passed)
	failed_amount = sum(1 for result in session.results.values() if result.failed)
	print(f'there are {passed_amount} passed and {failed_amount} failed tests')
