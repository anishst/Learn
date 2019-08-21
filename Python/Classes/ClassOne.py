class Calculator(object):

    #define class to simulate a simple calculator

    def __init__ (self):

        #start with zero
        self.current = 0

    def add(self, amount):

        #add number to current
        self.current += amount
 
    def Subtract(self, amount):

        #subtract number from current
        self.current -= amount

    def getCurrent(self):

        return self.current


cal1 = Calculator()
cal1.add(3)
print(cal1.current)
cal1.add(3)
print(cal1.current)