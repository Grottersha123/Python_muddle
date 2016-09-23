from PIL import Image
import os
def Convert(format,path):
	im = Image.open(path)
	f,e = os.path.splitext(path)
	out = f + '.'+format
	try:
	    im.save(out)
	except IOError:
	    print("cannot convert", path)
path = "D:\Python\Hurt.png"
Convert('tga',path)
