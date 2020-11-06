import shutil, os
from datetime import datetime
# recursively copy the entire directory tree rooted at src to dest. 
# dest must not already exist. 
source = r"c:\Temp\Python1"
dest = r"c:\Temp\Backup"
backupDir = os.path.join(dest,'backup' + datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
shutil.copytree(source, backupDir)