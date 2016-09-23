d = ['','one','two','three','four','five','six','seven','eight','nine']
tw = ['ten','eleven','twelve','thirteen','fourteen','fiveteen','sixteen','seventeen','eighteen','nineteen']
th = ['','','twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninety']

def name_that_number(x):
    if x == 0:
        return 'zero'
    if x // 10 == 0:
        return d[x]
    if x // 10 == 1:
        return tw[x%10]
    else:
        if x % 10 == 0:
            return th[x // 10]
        else:
            return th[x // 10] + ' '+ d[x%10]
    
def two_highest(list_):
    a = set(list_)
    a = list(a)
    m = []
    m.append(max(a))
    a.remove(max(a))
    m.append(max(a))
    return m
a = {'D': 'δ', 'E': 'ε', 'W': 'ω', 'N': 'η', 'B': 'β', 'T': 'τ', 'K': 'κ', 'Y': 'γ', 'P': 'ρ', 'X': 'χ', 'R': 'π', 'I': 'ι', 'V': 'υ', 'U': 'μ', 'A': 'α', 'O': 'θ','C':'c','F':'f','G':'g','H':'h','J':'j','L':'l','M':'m','Q':'q','S':'s','Z':'z'}
def gr33k_l33t(string):
    b = ''
    for i in string:
        b+= a[i.upper()]
    return b
        
