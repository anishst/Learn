# https://www.youtube.com/watch?v=k8asfUbWbI4&feature=push-u&attr_tag=W1dhq22Wik4lpJJI-6
import datetime
import calendar


balance = 10000
interest_rate = 13 * .01
monthly_payment = 200

# get today's date
today = datetime.date.today()

# monthrange returns a tuple, first day of month and last day of month

# get last day of month
days_in_current_month = calendar.monthrange(today.year, today.month)[1]
days_till_end_of_month = days_in_current_month - today.day


start_date = today + datetime.timedelta(days=days_till_end_of_month + 1)
end_date = start_date

while balance > 0:
	interest_charge = (interest_rate / 12) * balance
	balance += interest_charge
	balance -= monthly_payment

	# option 1	
	# balance = 0 if balance < 0 else round(balance,2)
	# option 2
	balance = round(balance,2)
	if balance < 0:
		balance = 0

	print(end_date, balance)
	
	days_in_current_month = calendar.monthrange(end_date.year, end_date.month)[1]
	end_date = end_date + datetime.timedelta(days=days_in_current_month)




 