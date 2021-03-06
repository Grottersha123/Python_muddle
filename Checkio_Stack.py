"""

В информатике стеком (stack) называют специализированный тип данных или контейнер, в котором реализованы две основных операции: добавление элемента в коллекцию (обычно именуют push) и удаление элемента из коллекции (обычно именуют pop). Реализация push и pop операций позволяет рассматривать стек как структуру данных, построенную в соответствии с принципом "последним пришёл - первым ушёл" (Last-In-First-Out, LIFO). В структуре данных LIFO первым (или верхним) элементом, доступным для удаления, должен быть элемент, который был добавлен последним. Кроме того, часто реализуется операция, возвращающая значение верхнего элемента без удаления его из коллекции.

Мы промоделируем работу стека на Питоне. Вам передается последовательность команд: - "PUSH X" -- добавить X (типа число) в стек. - "POP" -- получить значение верхнего элемента и удалить его из стека. Если стек пуст, операция возвращает 0 (ноль) и больше ничего не делает. - "PEEK" -- получить значение верхнего элемента. Если стек пуст, операция возвращает 0 (ноль).

Вы должны обработать все команды и просуммировать все цифры, которые были получены из стека (операциями "PEEK" или "POP"). Начальное значение суммы - 0 (ноль).

Давайте рассмотрим пример, дана следующая последовательность команд:
["PUSH 3", "POP", "POP", "PUSH 4", "PEEK", "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"]

Команда	Стек	Сумма
PUSH 3	3	    0
POP				0+3
POP				3+0
PUSH 4	4	     3
PEEK	4	     3+4
PUSH 9	4,9	7
PUSH 0	4,9,0	7
PEEK	4,9,0	7+0
POP		4,9		7+0
PUSH 1	4,9,1	7
PEEK	4,9,1	7+1=8
Вход: Последовательность комманд в виде списка строк.

Выход: Сумма полученных цифр в виде целого числа.

Пример:

digit_stack(["PUSH 3", "POP", "POP", "PUSH 4", "PEEK", "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"]) == 8
digit_stack(["POP", "POP"]) == 0
digit_stack(["PUSH 9", "PUSH 9", "POP"]) == 9
digit_stack([]) == 0
    
Как это используется: Стеки находят широкое примение. Мы видим стеки в повседневной жизни, от книг в нашей библиотеке и до чистых листов в лотке принтера. Все они следуют логике "последним пришёл - первым ушёл". То есть, когда мы добавляем книгу в стопку, мы кладем её наверх, и в свою очередь убирая книгу из стопки, мы, как правило, снимаем её с верха стопки.

Предусловия:
0 ≤ len(commands) ≤ 20;
all(re.match("\APUSH \d\Z", c) or с == "POP" or c == "PEEK" for c in commands)
"""

def digit_stack(List):
	stack = []
	sum = 0 # наша сумма 
	for i in List: # проходим по всему списку
		if ('PUSH 'in  i):
			a = [int(s) for s in i.split() if s.isdigit()] # выбирает все числа изстроки  и преобразует в тип число
			stack = a+stack # складываем значчение в стек
		if (i =='POP'): 
			if(len(stack) != 0): # проверяем наш стек есть ли там хоть  что-то
				sum+=stack.pop(0) # удаляем первый эелмент стека и добавляем его в сумму
			else:
				sum += 0 # если вдруг стек наш пуст то добавляем в смму ноль
		if (i == 'PEEK'):
			if(len(stack) != 0): # тоже самая проверка на то есть ли что-то в строчке
				sum+=stack[0] # первое значение списка добавляем в нашу сумму
			else:
				sum +=0
	return sum
			

a = digit_stack([])
print (a)


