import os
import time
import datetime
import platform

path_to_file = r'C:\Python\MyScripts\OracleDB\DOI IMAGE MIGRATION\2017-10-24 201745_CHECK_IMAGE_MIGRATION.xlsx'


def creation_date(path_to_file):
    """
    Try to get the date that a file was created, falling back to when it was
    last modified if that isn't possible.
    See http://stackoverflow.com/a/39501288/1709587 for explanation.
    """
    if platform.system() == 'Windows':
        return os.path.getctime(path_to_file)
    else:
        stat = os.stat(path_to_file)
        try:
            return stat.st_birthtime
        except AttributeError:
            # We're probably on Linux. No easy way to get creation dates here,
            # so we'll settle for when its content was last modified.
            return stat.st_mtime


print(creation_date(path_to_file))

(mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(path_to_file)
print("last modified: %s" % time.ctime(mtime))


def print_all_dates(filename):
    modifiedDate = os.path.getmtime(filename)
    CreatedDate = os.path.getatime(filename)
    ctime = os.path.getctime(filename)
    print(datetime.datetime.fromtimestamp(modifiedDate), datetime.datetime.fromtimestamp(
        CreatedDate), datetime.datetime.fromtimestamp(ctime))


def modification_date(filename):
    t = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(t)


print(modification_date(
    r'C:\Python\MyScripts\OracleDB\DOI IMAGE MIGRATION\2017-10-24 201745_CHECK_IMAGE_MIGRATION.xlsx'))

print(print_all_dates(r'C:\Users\532975\Downloads\IMG_0486.JPG'))
