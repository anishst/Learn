import glob
from PIL import Image
# random images: https://picsum.photos/
# https://stackoverflow.com/questions/753190/programmatically-generate-video-or-animated-gif-in-python
# filepaths
fp_in = "./pics/image*.jpg"
fp_out = "image.gif"

# https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#gif
img, *imgs = [Image.open(f) for f in sorted(glob.glob(fp_in))]
img.save(fp=fp_out, format='GIF', append_images=imgs,
         save_all=True, duration=200, loop=0)