# CBT nuggest video: https://www.youtube.com/watch?v=uJ-kwDo5b_c&t=504s
# decorator is a function that takes another function as its arguement
# A decorator is a function that accepts a function as input and returns a new function as output.



def makebold(fn):
	def wrapped():
		return "<strong>" + fn() + "</strong>"
	return wrapped

def makeitalics(fn):
	def wrapped():
		return "<i>" + fn() + "</i>"
	return wrapped

# using  decorator

@makebold	
@makeitalics
def hello():
	return "hello world"

print(hello())


