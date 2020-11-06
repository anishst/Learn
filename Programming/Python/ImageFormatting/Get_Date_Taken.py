# http://www.litster.org/blog/2010/05/30/python-and-exif-metadata-theres-more-than-one-way-to-do-it/

from PIL import Image
from PIL.ExifTags import TAGS
import glob, os,time

def get_exif(fn):
    ret = {}
    try:
        i = Image.open(fn)
        info = i._getexif()
        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            ret[decoded] = value
        return ret
    except Exception:
        return False


def RenameVideoFiles():
    counter = 1
    video_Description = "LeahBD"

    for img in glob.glob(r'E:\My Pictues\2016\Leah BD\*.m4v'):
        try:
            file, ext = os.path.splitext(img)
            dt = time.strftime('%Y%m%d',time.gmtime(os.path.getmtime(img)))
            print(dt)
            new_name = '{}{}{}{}{}'.format(time.strftime('%Y%m%d',time.gmtime(os.path.getmtime(img))),"_",video_Description, counter, ext)
            print(new_name)
            os.rename(img,os.path.join(os.path.dirname(img),new_name))   
            counter += 1 
        except Exception as e:
            print("There was an issue: {}".format(e))



def RenameImageFiles():

    pics_Description = "LeahBD"

    for img in glob.glob(r'C:\Users\532975\Documents\Automation\MyFramework\images\img1\*.JPG'):
        try:
            file, ext = os.path.splitext(img)
            
            #  get EXIF Data
            value = get_exif(img)
            # print(value['Model'])

            #  get created date 
            dateTaken =  value['DateTimeOriginal'].strip()
            dateTaken = dateTaken.replace(':',"")
            dateTaken = dateTaken.replace(' ',"_")
            print(dateTaken)
            new_name = '{}{}{}{}'.format(dateTaken,"_",pics_Description,ext)
            print(new_name)
            os.rename(img,os.path.join(os.path.dirname(img),new_name))
        except FileExistsError as ex:
        	print("test {}".format(ex))
        	# add code to move file to temp folder

        except Exception as e:
            # print(e)
            # print("last modified: %s" % time.ctime(os.path.getmtime(img)))
            # print("created: %s" % time.ctime(os.path.getctime(img)))
            dt = time.strftime('%Y%m%d',time.gmtime(os.path.getmtime(img)))
            print(dt)
            new_name = '{}{}{}{}'.format(time.strftime('%Y%m%d',time.gmtime(os.path.getmtime(img))),"_",pics_Description,ext)
            print(new_name)
            os.rename(img,os.path.join(os.path.dirname(img),new_name))

RenameImageFiles()
# RenameVideoFiles()