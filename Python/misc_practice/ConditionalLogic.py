#========================================
#   if statements
#========================================
a = 22
if a >= 22:
    print("if")
elif a >= 21:
    print("elif")
else:
    print("else")



def SecretNumber():
    One = int(input("Type num between 1 and 10: "))
    Two = int(input("Type num between 1 and 10: "))

    if (One >=1) and (One <=10):
        if (Two >=1) and (Two <=10):
            print('Your secret number is: ' + str(One * Two))
        else:
            print("Incorrect second value")
    else:
        print("incorrect first value")

SecretNumber()