def find_digit(num, nth):
    #your code here
    n = str(abs(num))[::-1]
    if nth <= 0 :
        return -1
    if len(n) < nth:
        return 0
    return int(n[nth-1])
        
def f(a):
    b = ''.join(''.join(str(a).split(']')).split('[')).split(',')
    return [int(i)for i in b if i!=' '] if b!=['']else[]
    
def p(l):
    n_l = [y for x in list(zip(*l)) for y in x]
    l = [y*(-1) for x in l for y in x]
    return n_l== l
