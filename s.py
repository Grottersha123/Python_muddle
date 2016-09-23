# split the image into individual bands
from PIL import Image
im = Image.open("D:\Python\Hurt.jpg")

source = im.split()

R, G, B= 0, 1, 2

# select regions where red is less than 100
mask = source[R].point(lambda i: i < 100 and 255)

# process the green band
out = source[G].point(lambda i: 255 - i)

# paste the processed band back, but only where red was < 100
source[G].paste(out, None, mask)

# build a new multiband image
im = Image.merge("RGB", source)

im.show()