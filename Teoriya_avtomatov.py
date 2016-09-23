

d={'1':'I','4':'IV','5':'V','9':'IX','10':'X','50':'L','90':'XC','100':'C','900':'CM','1000':'M'}

for i in sorted(d):
	print(i)
def level(number):
	number = str(number)
	a = []
	l = len(number)-1
	for i in number:
		a.append(i+'0'*l)
		l-=1
	return a

def Roman_numerals(n):
	lst = level(n)
	emp = ''
	for i in sorted(d):
		print (d[i])
		if i in lst:
			emp+= d[i]
	return emp

print(Roman_numerals(10))









