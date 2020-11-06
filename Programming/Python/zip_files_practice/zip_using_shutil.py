# https://www.youtube.com/watch?v=z0gguhEmWiY

import shutil

# #  create zip file
# shutil.make_archive('another_zip_using_shutil', 'zip', 'files')
#
# # extract
# shutil.unpack_archive('another_zip_using_shutil.zip', 'another')

#  create tar file
shutil.make_archive('another_zip_using_shutil', 'tar', 'files')

# extract
shutil.unpack_archive('another_zip_using_shutil.tar', 'another_tar')