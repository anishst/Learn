import shutil
import os
filesList = os.listdir(r"C:\Users\532975\Downloads")
src = r"C:\Users\532975\Downloads"
destination = r"C:\Users\532975\Downloads\OLB Logs"
for files in filesList:
	if files.endswith(".pdf"):
		# shutil.copy(os.path.join(src,files),destination)
		shutil.move(os.path.join(src,files), destination)