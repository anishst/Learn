from functools import wraps
import logging

FORMAT = '%(asctime)s:%(levelname)s:%(message)s:%(module)s:%(filename)s:%(filename)s'
logging.basicConfig(filename='test.log',level=logging.INFO,format=FORMAT)


def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called with args {}".format(args))
        logging.info(func.__name__ + " was called with args {}".format(args))
        return func(*args, **kwargs)
    return with_logging

@logit
def addition_func(x):
   """Do some math."""
   return x + x

@logit
def myname(*names):
	print(names)
	logging.debug("Print was success")

result = addition_func(4)

myname('anish','ligy')