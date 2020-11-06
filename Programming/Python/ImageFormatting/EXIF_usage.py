# http://www.litster.org/blog/2010/05/30/python-and-exif-metadata-theres-more-than-one-way-to-do-it/

from PIL import Image
from PIL.ExifTags import TAGS
import glob, os,time

#  remove exif data
#  https://stackoverflow.com/questions/19786301/python-remove-exif-info-from-images
image_file = open('image_file.jpeg')
image = Image.open(image_file)

# next 3 lines strip exif
data = list(image.getdata())
image_without_exif = Image.new(image.mode, image.size)
image_without_exif.putdata(data)

image_without_exif.save('image_file_without_exif.jpeg')


