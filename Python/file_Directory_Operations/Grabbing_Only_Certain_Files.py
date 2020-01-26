from PIL import Image
import os, os.path
from PIL.ExifTags import TAGS
 
def get_exif(fn):
    ret = {}
    i = Image.open(fn)
    info = i._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value
    return ret
 
 
def image_rename(path, filename):
    """
    This fucntion will rename image files using EXIF data
 
    Format: YYYY-MM-DD-HH-MM-SS_ImageDescription.ext
 
    """
    try:
        print(filename)
 
        # store filename and extension in 2 variables
        file_name, file_ext = os.path.splitext(filename)
 
        imageInfo = get_exif(os.path.join(path, file))
        # print(imageInfo['Model'])
        print(imageInfo['DateTimeOriginal'])
        dateval =  str(imageInfo['DateTimeOriginal'])
        dateval = dateval.replace(':',"")
        dateval = dateval.replace(' ',"_")
        phone_model = imageInfo['Model']
        print(dateval)
 
        new_name = '{}-{}-{}'.format(dateval, phone_model,file_ext)   
        os.rename(os.path.join(path, file), os.path.join(path, new_name))
 
   
    except Exception as e:
        print(e)
        # new_name = '{}-{}-{}'.format(file, 'NO_INFO_img',file_ext)   
        # os.rename(os.path.join(path, file), os.path.join(path, new_name))
 
        # new_name = '{}-{}'.format(imageInfo['DateTimeOriginal'], 'img')
 
 
def image_thumbnail(f,size):
    print(size)
    im = Image.open(f)
    im.thumbnail(size)
    im.save(f + "_THUMBNAIL_.png", format='PNG')
 
def image_resize(filename):
    im = Image.open(filename)
    image_size = width, height = im.size
    print(image_size)
    image_size = int(image_size[0]/2), int(image_size[1]/2)
    print(image_size)
    f_path, f_ext = os.path.splitext(filename)
    new_name = '{}_RESIZED_{}'.format(f_path,f_ext)
    print(new_name)
    im.resize(image_size).save(new_name, format='jpeg')
 
# ***********************************************************************
#       MAIN PROGRAM
# ***********************************************************************
size = 500, 500
imgs = []
path = r"E:\My Pictues\Home\Bathroom Update"
# path = r'C:\Users\532975\Downloads'
valid_images = [".jpg",".gif",".png",".tga",".jpeg"]
for file in os.listdir(path):
    ext = os.path.splitext(file)[1]
    if ext.lower() not in valid_images:
        continue
    filename = os.path.join(path, file)
 
    # FUNCTIONS
    # image_thumbnail(filename,size)
    image_resize(filename)
    # image_rename(path, file)