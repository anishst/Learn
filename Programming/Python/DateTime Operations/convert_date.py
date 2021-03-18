date_string = '3/21/2018 12:22'
from datetime import  datetime

date_obj = datetime.strptime(date_string, '%m/%d/%Y %H:%M')
print(date_obj)
# get date only
print(date_obj.date())

# get date only
print(date_obj.today())