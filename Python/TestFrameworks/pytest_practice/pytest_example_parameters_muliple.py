import pytest

@pytest.mark.parametrize("type_of_deposit", ['usc', 'fc', 'fcheck'])
@pytest.mark.parametrize("dep_type", ['draft', 'submit']
	)
def test_sample(type_of_deposit, dep_type):
	print(type_of_deposit, dep_type)