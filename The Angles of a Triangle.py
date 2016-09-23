
import math
def checkio(a,b,c):
	try:
		fisrt = round(math.acos((b**2 + c**2 - a**2)/(2*b*c)) * 180/math.pi)
		second =round(math.acos((a**2 + c**2 - b**2)/(2*a*c)) * 180/math.pi)
		f= 180-(fisrt + second)
		if a < b + c and b < a + c and c < a + b:
			return [0,0,0]
	except:
		return [0,0,0]
a = checkio(10,20,30)
print(a)
