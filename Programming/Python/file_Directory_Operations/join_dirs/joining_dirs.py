import os, sys

get_current_file_dir = os.path.dirname(__file__)
print(get_current_file_dir)
folder1_path = os.path.join(get_current_file_dir, 'DataFiles', 'folder1')
print(folder1_path)
for file in os.listdir(folder1_path):
    print(file)
    print(os.path.join(folder1_path, file))

# using path lib
# https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f
print("using path lib...")
from pathlib import Path
folder1_path = Path("DataFiles")
print(folder1_path)
for file in os.listdir(folder1_path):
    print(file)
    print(os.path.join(folder1_path, file))






