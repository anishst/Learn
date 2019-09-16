import time
def clock(func):
	def clocked(*args): #
		t0 = time.perf_counter()
		result = func(*args) #
		elapsed = time.perf_counter() - t0
		name = func.__name__
		arg_str = ', '.join(repr(arg) for arg in args)
		print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
		return result
	return clocked


def clock_simple(func):
	def clocked(*args): #
		t0 = time.perf_counter()
		result = func(*args) #
		elapsed = time.perf_counter() - t0
		name = func.__name__
		arg_str = ', '.join(repr(arg) for arg in args)
		print(f"It took {elapsed} seconds to run", result)
		return result
	return clocked	


@clock
def snooze(seconds):
	time.sleep(seconds)
@clock
def factorial(n):
	return 1 if n < 2 else n*factorial(n-1)

@clock_simple
def delayTest():
	print("starting time")
	time.sleep(5)
	return "hello"


if __name__=='__main__':
	print('*' * 40, 'Calling snooze(.123)')
	snooze(.123)
	print('*' * 40, 'Calling factorial(6)')
	print('6! =', factorial(6))

	print(delayTest())