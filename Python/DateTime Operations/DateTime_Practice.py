import time #https://docs.python.org/2/library/time.html
import datetime
from datetime import timedelta

# strftime   #https://docs.python.org/2/library/time.html#time.strftime
print(time.strftime("%m/%d/%Y"))   

print(time.strftime("%Y-%m-%d"))

print(time.strftime("%d-%m-%Y %H:%M:%S %p")) # timestamp
print(time.tzname)
print(time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime()))

# datetime related https://docs.python.org/2/library/datetime.html
print(datetime.date.today())


print("Counting time until")
today = datetime.date.today()
nyd = datetime.date(2019, 1,1)
print("There are ",(nyd-today).days, " days until {} ".format(nyd))

print("Show elapsed days")
today = datetime.date.today()
nyd = datetime.date(2018,10,1)
print("It has been ",(today-nyd).days, " days since {} ".format(nyd))


bd = datetime.date(1979,7,1)
today = datetime.date.today()
print("You are ",(today-bd).days, " days old")

print("**** subtract days from date ***")
print(datetime.date.today() - timedelta(days=10))
print(datetime.date.today() - timedelta(days=365*7))

# Script execution time 
# method 1
print("Testing Timing Script")
start_time = time.time()
time.sleep(3)
print("Script completed in: {:.2f} seconds".format(time.time() - start_time))

# method 2
import timeit
start_time = timeit.default_timer()
# code you want to evaluate
time.sleep(3)
elapsed = timeit.default_timer() - start_time
print(elapsed)

