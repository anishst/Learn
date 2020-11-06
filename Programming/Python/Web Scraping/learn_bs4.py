import re
import requests
from bs4 import BeautifulSoup

URL = 'https://www.johnlewis.com/technics-sc-c50-ottava-s-premium-hi-fi-system-with-bluetooth-wi-fi-chromecast-airplay/p3775230'
TAG_NAME = "p"
QUERY = {"class": "price price--large" }
response = requests.get(URL)
content = response.content
soup = BeautifulSoup(content, 'html.parser')
element = soup.find(TAG_NAME, QUERY)
string_price = element.text.strip()
print(string_price)

# format price; comma is optional
pattern = re.compile(r"(\d+,?\d*\.\d\d)")
match = pattern.search(string_price)
found_price = match.group(1)
found_price = found_price.replace(",","")
price = float(found_price)
print(price)