"""
Для практики в лингвистике Роботы хотят изучить суффиксы.

В этой задаче дан набор слов в нижнем регистре. Проверьте есть ли в этом наборе пара слов, такая что одно слово заканчивается другим (суффикс или совпадение). Для примера: {"hi", "hello", "lo"} -- "lo" это окончание "hello", так что результат True.

Замечания: Для этой задачи вы можете прочитать о типе данных set и строковых функциях.

Вх. данные: Слова как набор (set) строк (str).

Вых. данные: True или False, как булево выражение.

Примеры:

checkio({"hello", "lo", "he"}) == True
checkio({"hello", "la", "hellow", "cow"}) == False
checkio({"walk", "duckwalk"}) == True
checkio({"one"}) == False
checkio({"helicopter", "li", "he"}) == False
    
1
2
3
4
5
6
Как это используется: В этой задаче вы познакомитесь с тем, как итерировать тип данных set и некоторыми полезными функциями.

Предусловия: 2 ≤ len(words) < 30
all(re.match(r"\A[a-z]{1,99}\Z", w) for w in words)
"""

def checkio(Se):
	a = list(Se)
	if len(Se) == 1:
		return False
	else:
		for i in Se:
			for j in Se:
				if i == j:
					continue
				if i.endswith(j):
					return True
					break
	return False
				


a = checkio({"hello","llo"})
print(a)
