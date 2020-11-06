from datetime import datetime
from pytz import timezone

local_date_time = datetime.today()
print(local_date_time)


from time import gmtime, strftime
import time
print("\nGMT: "+time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime()))
print("Local: "+strftime("%a, %d %b %Y %I:%M:%S %p %Z\n"))

import datetime

snapshot = datetime.datetime.now()
print(f"Local time {snapshot}")
print(f"GMT time {snapshot.utcnow()}")

print(datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f%Z"))

today = (datetime.date.today()).strftime("%m/%d/%Y")
print(today)
print(type(today))

date_time_str = '06/30/2020 15:40:59'
print(date_time_str)
date_time_obj = datetime.datetime.strptime(date_time_str, '%m/%d/%Y %H:%M:%S')
print(date_time_obj)
print(type(date_time_obj))
print(date_time_obj.utcnow())

snapshot = datetime.datetime.now()
print(f"Local time {snapshot.strftime('%m/%d/%Y %H:%M:%S')}")
print(f"GMT time {snapshot.utcnow().strftime('%m/%d/%Y %H:%M:%S')}")
print(f"GMT time - date only {snapshot.utcnow().strftime('%m/%d/%Y')}")

print(datetime.datetime.now(datetime.timezone.utc).strftime('%m/%d/%Y'))


