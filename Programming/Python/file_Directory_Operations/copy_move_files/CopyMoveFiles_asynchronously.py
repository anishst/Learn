# https://towardsdatascience.com/knowing-these-you-can-cover-99-of-file-operations-in-python-84725d82c2df
import shutil
import threading
import subprocess
import multip.\
    rocessing

src = "1.csv"
dst = "dst_thread.csv"

#  option 1
thread = threading.Thread(target=shutil.copy, args=[src, dst])
thread.start()
thread.join()



#  option 2
dst = "dst_multiprocessing.csv"
process = multiprocessing.Process(target=shutil.copy, args=[src, dst])
process.start()
process.join()

# option 3
cmd = "cp 1.csv dst_subprocess.csv"
status = subprocess.call(cmd, shell=True)
