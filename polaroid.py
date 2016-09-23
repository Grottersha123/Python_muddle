from math import pi
from math import sqrt
from math import asin
from math import log
def checkio(height,width):
	height = height/2
	width = width/2
	if height == width:
		return [round((height)**2 * pi*4,2),round((height)**3 * pi*(4/3),2)]
	if height > width:
		e = sqrt(height**2 - width**2)/height
		S = round(2*pi*width*(width + ((height*asin(e))/e)),2)
		V = round(4/3*pi*(height)*width**2,2)
		return [S,V]
	else:
		e = sqrt(width**2 - height**2)
		S = round(2*pi*width*(width + height**2/e * log((width + e)/height)),2)
		V = round(4*pi*width**2 * height/3,2)
		return [S,V]

print(checkio(10,10))
