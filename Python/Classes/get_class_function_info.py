# access individual


import inspect
import os


class MyClass(object):
    """The class's docstring"""

    def my_method(self):
        """The method's docstring"""


def my_function():
    """The function's docstring"""


# access functions docstring

print(my_function.__doc__)

print(my_function.__module__)

# get all docstrings from class
help(MyClass)
print(dir(MyClass))
#  get full path
print(__file__)
# get base name
print(os.path.basename(__file__))

# inspect.getfile(MyClass.__class__)
# inspect.getmodule(MyClass.__class__)


# method 1


def hello():
    frame, filename, line_number, function_name, lines, index = inspect.stack()[
        1]
    print(frame, filename, line_number, function_name, lines, index)


hello()

print("*" * 100)


def hello2():
    print(inspect.stack()[1][3])


hello2()
