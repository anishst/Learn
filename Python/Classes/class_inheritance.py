class Animal:

	def make_sound(self, sound):
		print(sound)

	cool = True

class Cat(Animal):
	pass

newcat = Cat()
newcat.make_sound('meow')
print(newcat.cool)
print(Animal.cool)
print(isinstance(newcat, object))
