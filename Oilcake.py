from fractions import Fraction

def gcd(a,b):
    while a!= b:
        if a > b:
            a = a-b
        else:
            b = b-a
    return a
            
    
def chekio(tup):
    a = [abs(i) for i in tup]
    all_pie = Fraction(sum(a),sum(a))
    part = 0
    s = 0
    for i in tup:
        if i > 0:
           all_pie = all_pie - Fraction(i,sum(a))
        if i < 0:
            all_pie = all_pie - Fraction(abs(i),sum(a))* all_pie
    if all_pie.numerator < 0 or all_pie.denominator < 0:
        return (0,1)
    return (all_pie.numerator,all_pie.denominator)
        
        
