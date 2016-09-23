def lol(a,b,op):
	return {'a':a&b,'l':a|b}[op]
a = lol(1,2,'a')
print (a)