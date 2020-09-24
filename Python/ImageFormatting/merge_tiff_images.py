from PIL import Image
from PIL import TiffImagePlugin
import os

list_file = os.listdir("./images")
print(list_file)
with TiffImagePlugin.AppendingTiffWriter("merged.tiff",True) as tf:
    for tiff_in in list_file:
        print(tiff_in)
        try:
            im= Image.open(os.path.join(os.getcwd(), "images",tiff_in))
            im.save(tf)
            tf.newFrame()
            im.close()
            print("Success!")
        except Exception as e:
            print(f"Error! {e}")