import pytest

@pytest.mark.usefixtures("setup")
@pytest.mark.usefixtures("data_load")
class TestDataLoad():

	def test_print_user_info(self, data_load):
		print(data_load)






