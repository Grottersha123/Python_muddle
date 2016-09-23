""""Fizz buzz" это игра со словами, с помощью которой мы будем учить наших роботов делению. Давайте обучим компьютер.

Вы должны написать функцию, которая принимает положительное целое число и возвращает:
"Fizz Buzz", если число делится на 3 и 5;
"Fizz", если число делится на 3;
"Buzz", если число делится на 5; 
Число, как строку для остальных случаев.
Входные данные: Число, как целочисленное (int).

Выходные данные: Ответ, как строка (str).

Примеры:checkio(15) == "Fizz Buzz"
checkio(6) == "Fizz"
checkio(5) == "Buzz"
checkio(7) == "7"
"""
def checkio(n):
	if (n % 3 == 0) & (n % 5 == 0) & (n != 0):
		return "Fizz Buzz"
	if (n % 3 == 0) & (n != 0):
		return "Fizz"
	if (n % 5 == 0) & (n != 0):
		return "Buzz"
	else:
		return n
for i in range(20):
	print (checkio(i))
