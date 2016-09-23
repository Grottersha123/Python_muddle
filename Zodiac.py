a = ['Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 'Goat', 'Monkey', 'Rooster', 'Dog', 'Pig']
e = ['Wood', 'Fire', 'Earth', 'Metal', 'Water']

def chinese_zodiac(year):
    l = year-1984
    c = 0
    while l > 12:
        l-= 12
        c += 1
        print(c)
    while c > 5:
        c-= 5
    print(c)

def s(st):
    i= 0
    a = []
    b = True
    while i < len(st) and b:
        sym = st[i]
        if sym == '(':
            a.append(sym)
        else:
            if a == []:
                b = False
            else:
                a.pop()
        i = i + 1
    return b and not (a)
            
def s1(st):
    a = []
    for i in st:
        a.append(i)
    for i in range(len(a)+1):
        if a[i] == '(':
            for j in range(len(a)):
                if a[j] == ')':
                    print (a[j])
                    a.pop(i)
                    a.pop(j)
    return a
        
def dec(n):
    a = []
    k = ''
    while n > 0:
        rm = n % 2
        a.append(str(rm))
        n = n // 2
    while a != []:
        k += a.pop()
    return k

def d(n,b):
    a = []
    string = '0123456789ABCDF'
    k = ''
    while n > 0:
        rm = n % b
        a.append(rm)
        n = n // 2
    while a != []:
        k += string[a.pop()]
    return k
    
