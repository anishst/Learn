# https://holypython.com/image-manipulation-with-python-pil/

from PIL import Image, ImageEnhance
from PIL import ImageFilter

f = r"C:\Users\anish\Downloads\IMG_9132.JPG"
img = Image.open(f)
img.show()
# emboss
# img2 = img.filter(ImageFilter.EMBOSS)
# img2.show()

# img2 = img.filter(ImageFilter.CONTOUR)
# img2.show()

# img2 = img.filter(ImageFilter.SHARPEN)
# img2.show()

# img2 = img.filter(ImageFilter.MaxFilter(size=3))
# img2.show()

# img3 = img.filter(ImageFilter.MinFilter(size=3))
# img3.show()

# applier = ImageEnhance.Sharpness(img)
# applier.enhance(10).show()

# applier = ImageEnhance.Color(img)
# applier.enhance(0.5).show()

#  brightness
# applier = ImageEnhance.Brightness(img)
# applier.enhance(1).show()

# contrast
# applier = ImageEnhance.Contrast(img)
# applier.enhance(1).show()

# color
#An .enhance() value of 1 will apply original colors, 0 will give black&white, 100 will blow out the colors and 0.5 will be half way into a black&white image.
#If you’d like to save an image just apply .save() method instead of .show()
applier = ImageEnhance.Color(img)
applier.enhance(1.2).show()
