# ========================================
# Python strings - https://docs.python.org/2/library/string.html
# ========================================
import time
stringVar = 'testing strings'
# counts the number of occurrences of 'x' in stringVar
print(stringVar.count('i'))
print(stringVar.find('t'))  # returns the position of character 'x'
# returns the stringVar in lowercase (this is temporary)
print(stringVar.lower())
# returns the stringVar in uppercase (this is temporary)
print(stringVar.upper())
# replaces all occurrences of t with q in the string
print(stringVar.replace('t', 'q'))
print(stringVar.strip())  # removes leading/trailing white space from string
print(stringVar.title())

# mutiline string - using triple quotes
strmulti = '''This is a multi-line string. This is the first line.
This is the second line.
"What's your name?," I asked.
He said "Bond, James Bond."
'''
print(strmulti)

# string indexes
a = "string"
print(a[1:3])  # grab range of string
print(a[:-2])

# **********************************************************************************************************
# String Formatting
# **********************************************************************************************************
# formatting integers
print("Binary representation of {0} is {0:b}".format(12))
# formatting floats
print("Exponent representation: {0:e}".format(1566.345))
# round off
print("One third is: {0:.3f}".format(1/3))
# string alignment
print("|{:<10}|{:^10}|{:>10}|".format('butter', 'bread', 'ham'))

# format methods
age = 20
name = 'anish'
print('{0} was {1} years old when he wrote this book'.format(name, age))
print('Why is {0} playing with that python?'.format(name))
age = 20
name = 'anish'
print('{} was {} years old when he wrote this book'.format(name, age))
print('Why is {} playing with that python?'.format(name))


# Python Formatting
print('The order total comes to %f' % 123.44)
print('The order total comes to %.2f' % 123.444)  # formatting numbers
a = "abcdefghijklmnopqrstuvwxyz"
print('%.20s' % a)  # limiting a to 20 chars


# Print will all print on a separate line each. To prevent this newline character from being printed, you can specify that it should end with a blank:
print('a', end='')
print('b', end='')
# end with a space
print('a', end=' ')
print('b', end=' ')
print('c')

# **********************************************************************************************************
# Common Python String Methods
# **********************************************************************************************************

mystring = "Testing | string | methods"
print("***************** # Common Python String Methods ****************************")
print(mystring)
print(mystring.find("s"))
print(mystring.replace("s", "t"))
print(mystring.lower())
print(mystring.upper())

# break up a long print statement over several lines
# print("Anish's fav lan is: " +
# 	favorite_languages['Anish'].title() +
# 	".")

# Padding Text
print('{:4d}'.format(42))

# at least 6 characters with 2 after the decimal point
print('{:06.2f}'.format(3.141592653589793))
print('{:04d}'.format(42))
print('{:+d}'.format(42))
print('{:*^50}'.format(' centered '))
print('{:*^50}'.format(''))
string1 = "testing"
string2 = "testing2"
print('{}{:*^50}{}'.format('', string1, string2))
print(format(5, "05d"))

# add 1000 sep
print('{:,}'.format(40000))
# using f-string
val = 4000000000.89
print(f'{val:,}')

for i in range(2):
    print("Binary representation of {0} is {0:b}".format(i))

# https://docs.python.org/3.6/library/stdtypes.html?highlight=zfill#str.zfill
test_zfill = "45"
print(test_zfill.zfill(4))
print("-42".zfill(5))


print('{message:{fill}{align}{width}}'.format(
    message='Hello12345', fill="*", align='^', width=25))

#  find the last item after a certain char
mystring = "232323/afsfs"
print(mystring.find('/'))
print(mystring[mystring.find('/')+1:])

#  Test results
print("Test results formatting")
emailbody = '+{message:{fill}{align}{width}}+\n'.format(
    message='', fill="-", align='^', width=100)
emailbody += '+{message:{fill}{align}{width}}+\n'.format(
    message='STABILTY RESULTS', fill=".", align='^', width=100)
emailbody += '+{message:{fill}{align}{width}}+\n'.format(
    message='http://qae.otcnet.fms.gov', fill=".", align='^', width=100)
emailbody += '+{message:{fill}{align}{width}}+\n'.format(message=str(
    time.strftime("%d-%m-%Y %H:%M:%S %p")), fill=".", align='^', width=100)
emailbody += '+{message:{fill}{align}{width}}+\n'.format(
    message='', fill="-", align='^', width=100)
emailbody += '|{message:{fill}{align}{width}}|'.format(
    message='TestModule', fill="", align='^', width=50)
emailbody += '{message:{fill}{align}{width}}|\n'.format(
    message='Status', fill="", align='^', width=49)
emailbody += '+{message:{fill}{align}{width}}+\n'.format(
    message='', fill="-", align='^', width=100)
emailbody += '|{message:{fill}{align}{width}}|'.format(
    message='TestModule', fill="", align='^', width=50)
emailbody += '{message:{fill}{align}{width}}|\n'.format(
    message='Status', fill="", align='^', width=49)
emailbody += '+{message:{fill}{align}{width}}+\n'.format(
    message='', fill="-", align='^', width=100)
print(emailbody)
