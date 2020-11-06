# https://tinyjpg.com/
# https://tinypng.com/dashboard/developers

import tinify

tinify.key = "oYRgnqTIE2byKKX5VTSRmNRzcDI76gfl"
source = tinify.from_file("images/pngimg1.png")
source.to_file("images/optimized.png")