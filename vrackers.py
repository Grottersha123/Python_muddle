brackers = "[({"


def lol(b):
	stack = [] 
	for j in b:
		if j in brackers:
			stack.append(j) 
		if j == '}':
			if len(stack) <= 0  or stack[-1] != "{":
				return False
			stack.pop()
		if j == ')':
			if len(stack) <= 0  or stack[-1] != "(":
				return False
			stack.pop()
		if j == ']':
			if len(stack) <= 0  or stack[-1] != "[":
				return False
			stack.pop()
	return True

a = lol("(()(){})")
print (a)