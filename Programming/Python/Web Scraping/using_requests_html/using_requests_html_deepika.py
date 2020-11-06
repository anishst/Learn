# https://html.python-requests.org/

from requests_html import HTMLSession

session = HTMLSession()
r = session.get('https://english.deepika.com/MainNews.aspx', verify=False)

print(r.html.absolute_links)



# Grab an Element’s text contents:
news_links = r.html.find('.news_clr')
print(news_links)

for news in news_links:
	print(news.attrs)
	print(news.attrs['href'])
	print(news.full_text)
	print(news.absolute_links)





