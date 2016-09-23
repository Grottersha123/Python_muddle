open_b = "{[("
close_b = {'}':'{',']':'[',')':'('}
def checkio(data):
	stack = []
	for i in data:
		if i in open_b:
			stack.append(i)
		elif i in close_b:
			if not stack or stack[-1] !=close_b[i]:
				return False
			stack.pop()
	return not stack

print(checkio("1+2"))


