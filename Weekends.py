"""
София дала вам свое расписание и две даты и сказала, что ей нужно распланировать свои выходные. Она просит вас посчитать, сколько выходных (Суббота и Воскресение) будет начиная с первой даты и оканчивая второй. Если граничные даты выпадают на выходной, то считайте их тоже.

Даты даны, как тип данных datetime.date (Подробней можете прочитать здесь). Результат должен быть целым числом.

Входные данные: Начальная и окончательная дата, как datetime.date.

Выходные данные: Количество выходных дней между этими датами, как целое число (int).

Примеры:

checkio(date(2013, 9, 18), date(2013, 9, 23)) == 2
checkio(date(2013, 1, 1), date(2013, 2, 1)) == 8
checkio(date(2013, 2, 2), date(2013, 2, 3)) == 2
1
2
3
Связь с реальной жизнью: Хорошая возможность научится работать с датами. Эти методы часто используются в календарных приложениях, в автоматических системах извещений и других подобных областях.

Предусловие: start_date < end_date.
"""
from datetime import date,timedelta
def checkio(f,s):
	days = 0
	delta = timedelta(1)
	while(f<=s):
		s-=delta
		#print(delta)
		if s.isoweekday() in (5,6):
			days+=1
			
	return days
a = checkio(date(2015, 2, 2), date(2015, 2, 3))
print(a)