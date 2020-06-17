import platform, os

driver = 'chrome'
print(os.name)
print(platform.system())
if platform.system() != 'Windows' and driver == 'chrome' or driver == 'msedge':
    print("check for these browsers")
else:
    print("Skipping test")