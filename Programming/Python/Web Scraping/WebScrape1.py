from bs4 import BeautifulSoup
import requests

url = "www.pythonforbeginners.com"
r  = requests.get("http://" +url)
data = r.text
soup = BeautifulSoup(data,"lxml")
for link in soup.find_all('a'):
    print(link.get('href'))