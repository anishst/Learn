import sys
with open('redirect2.txt', 'w') as f:
    sys.stdout = f
    print ("test")