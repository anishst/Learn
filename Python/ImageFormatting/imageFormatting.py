# https://pillow.readthedocs.io/en/4.1.x/handbook/index.html
# http://effbot.org/imagingbook/concepts.htm
# http://pillow.readthedocs.io/en/latest/reference/Image.html#PIL.Image.format
 
#  Notes:
#  thumbnail resizes in place, resize return the resized image
from PIL import Image
import glob, os
 
# im = Image.open("pic.png")
# print(im.format, im.size, im.mode)
# im.show() # open picture
 
def imageCrop(): # work in progress
 
    box = (100, 100, 400, 400)
    region = im.crop(box)
    # region.show()
    region.save("test.jpeg")
 
def imageThumbnail(): # working
    """This function resizes images"""
 
    #  list to store image names
    image_list = []
 
    #  max size for the resized image
    size = 1500,1500
 
    for img in glob.glob(r'E:\My Pictues\2016\Blizzard - Jan 2016\*.[jpg][png][gif]'):
        # get filename an extension
        file, ext = os.path.splitext(img)
        try:
            im = Image.open(img)
            #  ANTIALIAS applies high-quality downsampling filter 
            im.thumbnail(size, Image.ANTIALIAS)
            output_filename = file + "_THUMBNAIL_"+ ext
            print(output_filename)
            im.save(output_filename, im.format)
 
            # im.show()
            image_list.append(im)
            print("Created thumbnail for {}".format(img))
            im.close()

 
        except Exception as e:
            print("Something happened with {}: Error {}".format(img,e))

 
 
def imageDetails(): # FINAL
    for image in image_list:
        print(image.format)
        print(image.size) # 2-tubel(width, height)
        print(image.width)
        print(image.height)
        print(image.filename)
        print(image.info)
        #  display image
        image.show()
 
 
def imageResize(): # work in progress
 
    size = 500, 500
 
    for infile in glob.glob("images/*.*"):
        file, ext = os.path.splitext(infile)
        im = Image.open(infile)
        im.resize(size, Image.ANTIALIAS)
        im.save(file + ".PNG", format='PNG')
        # im.show()
        
 
# ////////////////////////////////////////////////////////////////
#           *** Main ****
# ////////////////////////////////////////////////////////////////
imageThumbnail()
# imageResize()