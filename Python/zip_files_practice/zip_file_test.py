# https://www.youtube.com/watch?v=z0gguhEmWiY
import zipfile

#  simple zip; no compression
# with zipfile.ZipFile('my_zip.zip', 'w') as my_zip:
#     my_zip.write('test.html')
#     my_zip.write('test.txt')
#
# #  with compression
# with zipfile.ZipFile('my_zip.zip', 'w', compression=zipfile.ZIP_DEFLATED) as my_zip:
#     my_zip.write('test.html')
#     my_zip.write('test.txt')
#
#
# # extract all files
with zipfile.ZipFile('my_zip.zip', 'r') as my_zip:
    # get file names
    print(my_zip.namelist())
    # extract all to files folder
    my_zip.extractall('files')

# # extract one single file
with zipfile.ZipFile('my_zip.zip', 'r') as my_zip:
    # extract one file
    my_zip.extract('test.txt')