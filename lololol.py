import sys
from PIL import Image
im1 = 'D:/Python/Pokemon/002.bmp'
im2 = 'D:/Python/Pokemon/001.bmp'
im_1 = Image.open(im1)
im_2 = Image.open(im2)
Image.alpha_composite(im_1,im_2).show()
