# List of free APIs: https://github.com/toddmotto/public-apis#finance
import json
import requests

r = requests.get('https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json')
r.raise_for_status()
# works for Python2 and Python3
data = json.loads(r.content.decode('utf-8'))
new_string = json.dumps(data, indent=2, sort_keys=True)
# print(new_string)
usd_rates = dict()

# loop to get all $1 RATES and store to dictonary
for item in data['list']['resources']:
    name = item['resource']['fields']['name']
    price = item['resource']['fields']['price']
    usd_rates[name] = price

# Loop thru usd_rates dict
# for name, price in usd_rates.items():
# 	print(name,price)

USD_amount = 12
for name, price in usd_rates.items():
	# print(name,price)
	try:
		if name == 'USD/INR':
			converted_amount = float(price) * USD_amount
			print("{} US Dollar is equal to {} {}".format(USD_amount,converted_amount, name.split('/')[1]))
	except Exception as e:
		print("{} Didn't work {}".format(name,e))

# converting given amount to converted amount
print(USD_amount * float(usd_rates['USD/INR']))

