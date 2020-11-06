# Exceptions
# https://docs.python.org/3/tutorial/errors.html

try:
    f = open("Test.txt")
    # var = 5/0
    pass
except FileNotFoundError:
    print("Sorry, This file does not exist")
except Exception as e:
    print("Error:{}".format(e))
else: # if no exceptions run this
    print(f.read())
    f.close()
finally: # run all time even if there is an error
    print("Executing Finally")
print("=================================================")
print(" EXAMPLE 2")
print("=================================================")
# handling exception example
var1 = '1' 
try:
    var2 = var1 + 1 # since var1 is a string, it cannot be added to the number 1 
except:
    var2 = int(var1) + 1 
print(var2)

try:
    #text = input('Enter something --> ')
    text = "testing exception handling"
except EOFError:
    print('Why did you do an EOF on me?')
except (KeyboardInterrupt, IOError): # More than one errors; treated as tuple
    print('You cancelled the operation.')
else:
    print('You entered {}'.format(text))

print("=================================================")
print(" EXAMPLE 3") # custom exceptions
print("=================================================")

class ShortInputException(Exception):
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    #text = input('Enter something --> ')
    text = "5"
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
    # Other work can continue as usual here
except EOFError:
    print('Why did you do an EOF on me?')
except ShortInputException as ex:
    print(('ShortInputException: The input was ' +
           '{0} long, expected at least {1}')
          .format(ex.length, ex.atleast))
else:
    print('No exception was raised.')


# ----------------
value = 2
exp_value =3

try:
    if value != exp_value:
        raise Exception("No match")
    else:
        print('match')
except Exception as e:
    print("issue")
