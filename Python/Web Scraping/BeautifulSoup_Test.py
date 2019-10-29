import requests
from bs4 import BeautifulSoup

my_url = 'http://www.fairfaxcounty.gov/business/'
r = requests.get(my_url)
#print(r.content)

soup = BeautifulSoup(r.content,"html.parser")
#print(soup.prettify())

# url substitution
links = soup.find_all("a")
for link in links:
	#if 'Language Translations' in link.text:
		print("<a href='%s'>%s</a>" %(link.get("href"),link.text))

# finding items by filtering tags and attributes
g_data = soup.find_all("div", {"id": "content"})

for item in g_data:
	print(item.text)