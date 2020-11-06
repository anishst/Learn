# https://html.python-requests.org/
# https://www.youtube.com/watch?v=a6fIbtFB46g&t=894s

# =============================================================================
# reading local HTML file
# =============================================================================
from requests_html import HTML

with open('simple_html_page.html') as html_file:
	source = html_file.read()
	html = HTML(html=source)

# print html
print(html.html)

#  print only text
print(html.text)

# find title
matches = html.find('h2')
print(matches)
print(matches[0].html)
print(matches[0].text)

for match in matches:
	print(match.text) 

# find title; return only the first match
match = html.find('title', first=True)
print(match.html)
print(match.text)

# find by id
match = html.find('#footer', first=True)
print(match.text)

# find by div
post = html.find('div.post', first=True)
print(post.text)
headline = post.find('h2', first=True).text
summary = post.find('p', first=True).text
print(headline, summary)

# looping 
print("Looping example")
posts = html.find('div.post')
for post in posts:
	headline = post.find('h2', first=True).text
	summary = post.find('p', first=True).text	
	print(headline, summary)
	print()