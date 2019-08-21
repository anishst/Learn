import datetime
import pytz
from tzlocal import get_localzone
from datetime import datetime

#  print local time
local_time_var = datetime.now()
print(f"Stored Local time: {local_time_var}")


#  print current utc time
utc_time_var = datetime.utcnow()
print(f"Stored UTC time: {utc_time_var}")


#  get local zone
local_tz = get_localzone()
print(local_tz)


#  display stored date in local
display_datetime_in_local = utc_time_var.replace(tzinfo=pytz.utc).astimezone(local_tz)
print(display_datetime_in_local )


eastern = pytz.timezone('US/Eastern')
amsterdam = pytz.timezone('Europe/Amsterdam')
display_amserdam_time = utc_time_var.replace(tzinfo=pytz.utc).astimezone(amsterdam)
print(f"Amsterdam :  {display_amserdam_time} ")

from pytz import all_timezones_set, common_timezones_set
for zone in common_timezones_set:
	time_zone = pytz.timezone(zone)
	print(f"Zone: {zone} Time: {utc_time_var.replace(tzinfo=pytz.utc).astimezone(time_zone)}")


