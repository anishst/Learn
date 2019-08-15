# https://docs.pytest.org/en/latest/reference.html#pytest-mark-parametrize
import pytest

# EXAMPLE 1
@pytest.mark.parametrize("test_input, expected_output",
	[
		(5,10),
		(2,4),
		(20,40)
	]
	)
def test_calc_square(test_input, expected_output):
	result = test_input * 2
	assert result == expected_output

#  EXAMPLE 2

@pytest.mark.parametrize("string_values", 
	[
		'test',
		'test2'
	])
def test_string_values(string_values):
	 print("hello " + string_values)


# EXAMPLE 3

@pytest.mark.parametrize("user_role",["HLAS", "CBAF"]) 
class TestOTCnetLogin():
    def test_Login(self, user_role):
        print("User Role: " + user_role)