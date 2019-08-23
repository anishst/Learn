class User:
	# class attribute to keep track of active users
	active_users = 0

	def __init__(self, first, last):
		self.first = first
		self.last = last
		User.active_users += 1

	def full_name(self):
		print(f"{self.first} {self.last}")

	def logout(self):
		User.active_users -= 1
		print(f"{self.first} logged out")


print(f"Active users: {User.active_users}")
user1 = User('Anish', 'Sebastian')
user2 = User('Ligy', 'Sebastian')
user1.full_name()
user2.full_name()
print(f"Active users: {User.active_users}")
user1.logout()
print(f"Active users: {User.active_users}")
user2.logout()
print(f"Active users: {User.active_users}")