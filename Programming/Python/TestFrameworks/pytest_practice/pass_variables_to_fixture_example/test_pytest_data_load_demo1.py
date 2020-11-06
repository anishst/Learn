import pytest
# https://docs.pytest.org/en/stable/fixture.html#factories-as-fixtures
@pytest.fixture()
def get_sessionid():
	print("Running helper ...")
	def _getenvid(env):
		return f"id of {env} is 12345"
	return _getenvid

def test_print_user_info(get_sessionid):
	sessionid = get_sessionid('qaef')
	print(sessionid)






