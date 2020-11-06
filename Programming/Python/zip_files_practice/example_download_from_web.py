import zipfile
import requests

# download a zip file
r = requests.get('https://github.com/anishst/Learn/archive/master.zip')

with open('data.zip', 'wb') as f:
    f.write(r.content)

with zipfile.ZipFile('data.zip', 'r') as data_zip:
    print(data_zip.namelist())