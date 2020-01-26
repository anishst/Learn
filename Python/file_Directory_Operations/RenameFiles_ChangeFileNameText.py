import os

os.chdir(r'C:\Users\532975\Documents\BAH Projects\OTCnet\Testing\Release 2.7\10 YEAR DATA RUN\After Purge\Deposits\temp')

for filename in os.listdir():
    print(filename)
    newname = filename.replace("NON_PURGE_ITEMS","suckers")
    print(newname) #should display AC-5400ES_manual.txt
    os.rename(filename, newname)