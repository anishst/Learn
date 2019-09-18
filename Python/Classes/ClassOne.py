class Calculator(object):

    # define class to simulate a simple calculator

    def __init__(self):

        # start with zero
        self.current = 0

    def add(self, amount):

        # add number to current
        self.current += amount

    def Subtract(self, amount):

        # subtract number from current
        self.current -= amount

    def getCurrent(self):

        return self.current

    def __str__(self):
        """string represenation"""
        return f"{self.current} is the current value and {type(self).__name__} is the name of class"


cal1 = Calculator()
cal1.add(3)
print(cal1.current)
cal1.add(3)
print(cal1.current)
print(cal1.__str__())
