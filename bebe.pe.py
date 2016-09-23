def lol(a):
	count = 0
	for i in range(2,a+1):
		if a % i == 0:
			count+= 1

	if count > 1:
		return False
	else:
		return True

def checkio(num):
    if lol(num) == True:
        return 0
    else:
        ans  = ''  
        digit = 9  
        while digit > 1:  
            if number%digit != 0:  
                digit -= 1  
            else:  
                ans = str(digit) + ans  
                number /= digit  
        if number == 1:  
            return int(ans)  
        else:  
            return 0
        
                
