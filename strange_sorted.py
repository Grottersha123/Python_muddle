"""
Давайте посмотрим на сортировку. Дан массив с особыми правилами.

Массив (tuple) содержит различные числа. Вам необходимо отсортировать их, но отсортировать на основе абсолютных значений в возрастающем порядке. Для примера, последовательность (-20, -5, 10, 15) будет отсортирована следующим образом (-5, 10, 15, -20). Ваша функция должна возвращать список (list) или кортеж (tuple).

Входные данные: Массив чисел как кортеж (tuple).

Выходные данные: Список (list) или кортеж (tuple) (но не генератор) отсортированный по абсолютным значениям чисел.

Дополнение: Результат вашей функции вы увидите как список (list) в панели выводов результатов проверки.

Примеры:

checkio((-20, -5, 10, 15)) == [-5, 10, 15, -20] # or (-5, 10, 15, -20)
checkio((1, 2, 3, 0)) == [0, 1, 2, 3]
checkio((-1, -2, -3, 0)) == [0, -1, -2, -3]
    
1
2
3
4
Зачем это нужно: Сортировка это часть очень многих задач, так что будет полезно понимать, как ее использовать.

Предусловия: len(set(abs(x) for x in array)) == len(array)
0 < len(array) < 100
all(isinstance(x, int) for x in array)
all(-100 < x < 100 for x in array)
"""

def checkio(array):
	a = sorted([abs(i) for i in array])
	b = list(array)
	for i in range(len(a)):
		for j in range(len(b)):
			if (a[i] + b[j]) == 0:
				a[i] = b[j]
	print(a)



			
checkio((23,-5,1,0))