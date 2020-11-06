import os
import subprocess

path = r"D:\GitHub\Automation"
download_location = r"D:\TEMP"

md_notes_files = []
for dirpath, subdirs, files in os.walk(path):
    for x in files:
        if x.endswith("_notes.md"):
            # last dir
            # print(dirpath.split("\\")[-1])
            # dir starting after learn folder
            file_path = ((dirpath.split("\\"))[3:])
            URL = f"""https://raw.githubusercontent.com/anishst/Automation/master/{"/".join(file_path)}/{x}"""
            print(URL)
            # os.chdir(download_location)
            # pipe = subprocess.Popen(["curl", URL, "-O"])
            md_notes_files.append(os.path.join(dirpath, x))

# https://github.com/anishst/Learn/blob/master/CloudComputing/AWS/aws_notes.md
# https://raw.githubusercontent.com/anishst/Learn/master/CloudComputing/AWS/aws_notes.md
print(md_notes_files)