# lambdas are functions without name
# alwasy used to return values; not for actions
# example 1
def add(x,y):
    return x+y
print(add(5,3))

# giving name to lambda
result = lambda x, y: x+y
print(result(5,3))

# example 2
def double(x):
    return x *2
# using list comprehension
sequence = [1,5, 3,2]
doubled = [double(x) for x in sequence]
print(doubled)
print(f"Using list comprehension: {doubled} ")
# using map 
doubled = map(double, sequence)
print(f"Using map function: {list(doubled)} ")

# lambda
doubled = [(lambda x: x *2)(x) for x in sequence]
print(f"Using lamda: {doubled} ")

# lambda with map function
doubled = map(lambda x: x *2, sequence)
print(f"Using lamda with map function: {list(doubled)} ")


# lambda with filter function
# remove even numbers
nums = range(10)
a = filter(lambda  x:x%2 !=0, nums)
print(list(a))