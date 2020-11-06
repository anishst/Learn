# https://docs.python.org/3.6/library/textwrap.html

"""
Default length is 70 chars per line

"""
import textwrap

def main():
	long_string = "The textwrap module provides some convenience functions, as well as TextWrapper, the class that does all the work. If you’re just wrapping or filling one or two text strings, the convenience functions should be good enough; otherwise, you should use an instance of TextWrapper for efficiency."
	
	width = 20

	wrapped_lines = textwrap.wrap(long_string) # returns a list with 

	for line in wrapped_lines:
		print(line)

	print("\n--------------------------------\n")

	print(textwrap.fill(long_string, width))

if __name__ == '__main__':
	main()

