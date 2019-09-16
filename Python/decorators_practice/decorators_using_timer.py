import time
from functools import wraps

def timethis(func):
	'''
	Decorator that reports the execution time.
	'''
	@wraps(func)
	def wrapper(*args, **kwargs):
		start = time.time()
		result = func(*args, **kwargs)
		end = time.time()
		print("Function ",func.__name__, "finished in ", end-start, 'seconds')
		return result
	return wrapper


#  using the decorator

@timethis
def countdown(n):
	""" Counts down """
	while n > 0:
		n -= 1
		print(n)

@timethis
def wait(sec):
	time.sleep(sec)


countdown(10000)
wait(5)