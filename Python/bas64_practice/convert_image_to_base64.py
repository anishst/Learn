import base64

image_file = 'google.png'

with open(image_file,'rb') as img_file:
    my_base64_string = base64.b64encode(img_file.read())

print(my_base64_string)

# print without b
print(my_base64_string.decode())

import base64
data_uri = base64.b64encode(open(image_file, 'rb').read()).decode('utf-8')
img_tag = '<img src="data:image/png;base64,{0}">'.format(data_uri)
print(img_tag)

html = '<html><head></head><body><h1>Base 64 </h1>'
html +=  img_tag
html += '</body></html>'

print (html)

# Write HTML String to file.html
with open("file.html", "w") as file:
    file.write(html)
