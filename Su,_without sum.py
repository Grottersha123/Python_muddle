
def lol(data,n,count):
    if n < 0:
        return count
	else:
		return lol(data,n-1,count+data[n])
def checkio(data):
    return lol(data,len(data)-1,0)

def lol(data,n,count):
	if n < 0:
		return count
	else:
		return lol(data,n-1,count+data[n])

def checkio(data):
	print (lol(data,len(data)-1,0))
checkio([1,2,3])