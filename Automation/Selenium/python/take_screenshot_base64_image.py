from selenium import webdriver
import time

driver = webdriver.Edge()
driver.get("https://developer.mozilla.org/en-US/docs/Learn")
base64_img = driver.get_screenshot_as_base64()
img_tag = '<img src="data:image/png;base64,{0}">'.format(base64_img)
print(img_tag)

html = '<html><head></head><body><h1>Base 64 </h1>'
html +=  img_tag
html += '</body></html>'
print(html)
driver.quit()

# Write HTML String to file.html
# with open("file.html", "w") as file:
#     file.write(html)