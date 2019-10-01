# http://www.thecodingcouple.com/watermark-images-python-pillow-pil/

from PIL import Image, ImageDraw, ImageFont
 
image = Image.open('images/jpgimg1.JPEG')
width, height = image.size
 
draw = ImageDraw.Draw(image)
text = "A watermark"
 
font = ImageFont.truetype('arial.ttf', 56)
textwidth, textheight = draw.textsize(text, font)
 
# calculate the x,y coordinates of the text
margin = 5
x = width - textwidth - margin
y = height - textheight - margin
 
# draw watermark in the bottom right corner
draw.text((x, y), text, font=font)
 
image.save('images/watermark_test.JPEG')