dig = ['th','st','nd','d','th','th','th','th','th','th','th']


def century (year):
    y = str(year+100)[0:2]
    t = 0
    if int(y)//10 == 1:
        return y + 'th'
    else:
        return y + dig[int(y)% 10]

print(century(2011))
        
    
