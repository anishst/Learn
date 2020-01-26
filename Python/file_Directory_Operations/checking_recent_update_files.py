import os, time
path = r"Test_Files/"
# path = r'C:\Users\532975\Downloads'
valid_images = [".txt"]
for file in os.listdir(path):
    ext = os.path.splitext(file)[1]
    if ext.lower() not in valid_images:
        continue
    filename = os.path.join(path, file)
    print(f"Files {filename}\tModified on: {os.stat(filename).st_mtime }")
    import datetime
    mtime = os.stat(filename).st_mtime
    timestamp_str = datetime.datetime.fromtimestamp(mtime).strftime('%Y-%m-%d-%H:%M')
    print(timestamp_str)
    # print("Recently modified files:")
    # if os.stat(filename).st_mtime < 3000:
    #     print(filename)
