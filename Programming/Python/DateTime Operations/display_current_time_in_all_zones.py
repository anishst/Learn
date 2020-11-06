import datetime
import pytz
from tzlocal import get_localzone
from datetime import datetime



current_datetime =datetime.utcnow()

from pytz import all_timezones_set, common_timezones_set
for zone in common_timezones_set:
	time_zone = pytz.timezone(zone)
	print(f"Zone: {zone}\tTime: {current_datetime.replace(tzinfo=pytz.utc).astimezone(time_zone)}")


