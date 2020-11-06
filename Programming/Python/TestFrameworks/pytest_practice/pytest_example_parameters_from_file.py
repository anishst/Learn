import pytest

#  SIMPLE
# @pytest_practice.mark.parametrize("username, password",
# 	[
# 		('user1', 'pwd1'),
# 		('user2', 'pwd2'),
# 		('user3', 'pwd3')
# 	]
# 	)
# def test_sample(username, password):
#     print(username, password)

#  using file
user_info = []
with open('userlist.txt') as login_file:
	user_info = login_file.readlines()

print(len(user_info))
@pytest.mark.parametrize("user_info", user_info)
def test_sample(user_info):
	print(user_info)
	username, password = user_info.split(',')
	print(username, password)