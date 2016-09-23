def pup(x):
	a = x
	if a < 0:
		return "You lose"
	else:
		while x!=1:
			x = x - 1
			a = a*x
		return a
x = int(raw_input("Enter you count: "))
print pup(x)