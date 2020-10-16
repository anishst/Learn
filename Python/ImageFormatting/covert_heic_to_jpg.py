import os

from PIL import Image
import pyheif
# https://pypi.org/project/pyheif/

root_dir= r"C:\Users\anish\Downloads"
for root, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith('.HEIC'):
            print(file)

        heif_file = pyheif.read(file)
        image = Image.frombytes(
            heif_file.mode,
            heif_file.size,
            heif_file.data,
            "raw",
            heif_file.mode,
            heif_file.stride,
            )

        image.save(f"{file}.jpg", "JPEG")
