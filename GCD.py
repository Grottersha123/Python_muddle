"""
Наибольший общий делитель (НОД), для двух и более целых чисел называется наибольшее число, которое делит каждое число из данных без остатка.

Даны несколько положительных чисел. Найдите НОД для этих чисел.

Входные данные: Различное число аргументов, как целые числа.

Выходные данные: Наибольший общий делитель, как целое число.

Примеры:

great_common_divisor(6, 4) == 2
great_common_divisor(2, 4, 8) == 2
1
2
Как это используется: НОД - это один из базисов для математического ПО.

Предусловия: 
1 < len(args) ≤ 10
all(0 < x ≤ 2 ** 32 for x in args)
"""

def gcd (a,b):
	while b:
		a , b=b , a % b
	return a 


def great_common_divisor(*args):
	ls = list(args)
	size = len(ls)
	if size == 2:
		return gcd(ls[0],ls[1])
	else:
		while len(ls) != 1:
			emp = []
			a = gcd(ls.pop(0),ls.pop(0))

			emp.append(a)
			ls = emp + ls
		return a
print(great_common_divisor(6,10,15))

