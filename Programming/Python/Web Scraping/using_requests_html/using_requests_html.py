# https://html.python-requests.org/

from requests_html import HTMLSession

session = HTMLSession()
r = session.get('https://python.org/')

# grab a list of all links
print(r.html.links)

# abosolute links
print(r.html.absolute_links)

# Select an Element with a CSS Selector

# Grab an Element’s text contents:
about = r.html.find('#about', first=True)
print(about.text)

# Introspect an Element’s attributes
print(about.attrs)

# Render out an Element’s HTML:
print(about.html)

