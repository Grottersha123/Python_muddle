data = [[1,2,3],[4,5,6]]
mat = []
for i in range(len(data[0])):
	row = []
	for j in data:
		print (i)
		row.append(j[i])
	mat.append(row)
