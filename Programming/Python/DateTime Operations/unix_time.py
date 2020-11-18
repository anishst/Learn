# method to convert date and time to an unix timestamp
from datetime import datetime

def to_epoch(date, time):
    try:
        timestamp = round(datetime.strptime('{} {}'.format(date, time), '%Y/%m/%d %H:%M:%S.%f').timestamp())
        return timestamp
    except ValueError:
        return round(datetime.strptime('2017/09/11 17:02:06.418', '%Y/%m/%d %H:%M:%S.%f').timestamp())