


def letter_queue(data):
	queue= []
	message = ''
	for i in data:
		if "PUSH"in i:
			a  = i.split()[1]
			queue.append(a)
		if "POP" == i:
			if len(queue) != 0:
				queue.pop(0)

	return ''.join(queue)
print(letter_queue(["POP", "POP"]))








