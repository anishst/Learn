from lxml import etree
from selenium import webdriver

browser = webdriver.Chrome()

browser.get('http://www.python.org')
tree = etree.HTML(browser.page_source)
print(tree)
all_links = tree.findall(".//a")
# get first link text
print(all_links[0].text)

# print all links
for link in all_links:
    print(link.text)
