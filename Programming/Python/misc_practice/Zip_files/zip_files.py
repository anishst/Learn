import shutil

# get archive format
from pathlib import Path
from zipfile import ZipFile

print(shutil.get_archive_formats())

# dirpath = r'C:\Users\532975\Documents\Automation\GitHub\Learn\Python\misc_practice\Zip_files'
# shutil.make_archive('test_zip', 'zip', base_dir=dirpath)


# To create a zip file that includes all the text files in the directory
with ZipFile('text_files.zip', 'w') as file:
    for txt_file in Path().glob('*.txt'):
        print(f"*Add file: {txt_file.name} to the zip file")
        file.write(txt_file)


# To unzip a file that is just created
with ZipFile('text_files.zip') as zip_file:
    zip_file.printdir()
    zip_file.extractall()