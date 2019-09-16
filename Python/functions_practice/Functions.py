#========================================
#   Functions
# fucntion - stand alone code block
# method - function that is bound to an object
# allows code reuse, hides complexity from users
# parameter - design time place holder
# argument - runtime data object
#========================================
def someFunction():
    print("boo")
someFunction()
#  variable argument

def DisplayMulti(ArgCount = 0, *VarArgs):
	print('You passed ' + str(ArgCount) + ' arguments.', VarArgs)


DisplayMulti(3,"hello",1,True)

# Prefer Exceptions to Returning  None
def divide(a,b):
	try:
		return True, a/b
	except ZeroDivisionError:
		return False, None
x,y = 0,5
sucess, result  = divide(x,y)
if not sucess:
	print("Invalid inputs")
else:
	print(divide(x,y))


# keyword arg examples
# https://docs.python.org/3.6/tutorial/controlflow.html#keyword-arguments
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")


