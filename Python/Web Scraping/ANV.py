import urllib.request
from bs4 import BeautifulSoup

url = "http://www.anvgroup.com/events/"
# url = "http://www.tastycircle.com/recipe/cherupayar-payasam/"
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,"lxml")
# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out
# get text
text = soup.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)

print(text.encode('utf-8'))