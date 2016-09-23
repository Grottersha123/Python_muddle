"""
Продолжим изучение слов. Даны две строки со словами, разделенными запятыми. Попробуйте найти что общего между этими строками. Слова внутри каждой строки не повторяются.

Ваша функция должна находить все слова, которые появляются в обеих строках. Результат должен быть представлен, как строка со словами разделенными запятыми и отсортированными в алфавитном порядке.

Замечания: Вы легко решите данную задачу при помощи нескольких функций: str.split, str.join и sorted. Также взгляните на тип данных - set.

Вх. данные: Два аргумента как строки (str).

Вых. данные: Общие слова как строка (str).

Примеры:

checkio("hello,world", "hello,earth") == "hello"
checkio("one,two,three", "four,five,six") == ""
checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two"
    
1
2
3
4
Как это используется: В этой задаче вы попрактикуетесь в работе с наборами и строками. И эти навыки будут полезными для лингвистического анализа.

Предусловия: 
Каждая строка содержит не более 10 слов.
Все слова разделены запятыми.
Все слова состоят только из латинских букв в нижнем регистре.
"""
def checkio(te1,te2):
	emp = []
	new1 = set(te1.split(','))
	new2 = set(te2.split(','))
	for i in new1:
		if i in new2:
			emp.append(i)														
	return ','.join(sorted(emp))

a = checkio("one,two,three", "four,five,six")
print (a)