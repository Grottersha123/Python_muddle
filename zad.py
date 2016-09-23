name = raw_input("Enter word ")
s2 = ""
for x in range(len(name)):
	s2 = s2 + name[ len(name)-1-x]
print s2