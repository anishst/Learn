# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
import datetime
import pytz
from datetime import datetime

my_time_zones = ['Asia/Calcutta', 'America/New_York']


for zone in my_time_zones:
	time_zone = pytz.timezone(zone)
	print(f"Zone: {zone}\tTime: {datetime.utcnow().replace(tzinfo=pytz.utc).astimezone(time_zone)}")
	# formatted version
	print(f"Zone: {zone}\tTime: {datetime.utcnow().replace(tzinfo=pytz.utc).astimezone(time_zone).strftime('%Y-%m-%d %I:%M:%S %p')}")

