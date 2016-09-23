def hamdist(str1, str2):
	count = 0
	a = bin(str1)[2:]
	b = bin(str2)[2:]
	a=a.zfill(max(len(a),len(b)))
	b = b.zfill(max(len(b),len(a)))
	print (b)
	print(a)
	for i in range(len(a)):
		if a[i] != b[i]:
			count +=1
	return count
print(hamdist(17,117))
print(bin(17^117).count("1"))
#print (bin(117 ^ 5))


