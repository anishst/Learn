import os
import pathlib


print(os.path.abspath('rename_files.py')) # absolute
print(os.path.relpath('rename_files.py')) # relative

# using pathlib

print(pathlib.Path('rename_files.py').absolute()) # absolute
print(pathlib.Path('rename_files.py')) # relative

# get parent
print(pathlib.Path('rename_files.py').parent)
print(pathlib.Path('rename_files.py').resolve().parent)
print(os.path.dirname(os.path.abspath('rename_files.py')))

