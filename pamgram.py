"""
Панграмма (Греческий:παν γράμμα, pan gramma, "каждая буква") или предложение состоящее из разных букв алфавита, используя каждую букву по крайней мере один раз. Возможно, вы знакомы с хорошо известными панграммами "Эй, жлоб! Где туз? Прячь юных съёмщиц в шкаф" или "Любя, съешь щипцы, — вздохнёт мэр, — кайф жгуч".

Для этого задания, вы будете использовать латинский алфавит (A-Z). У вас есть текст с латинскими буквами и знаками препинания. Вы должны проверить является ли предложение панграммой или нет. Регистр не имеет значения.

Входные данные: Текст как строка.

Выходные данные: Является предложение панграммой или нет как логическое.

Примеры:

check_pangram("The quick brown fox jumps over the lazy dog.") == True
check_pangram("ABCDEF.") == False
1
2
Как это используется: Панграммы используют для отображения шрифтов, тестирования оборудования, развития почерка, каллиграфии и набора текста на клавиатуре.

Предусловия:

all(ch in (string.punctuation + string.ascii_letters + " ") for ch in text)
0 < len(text)

"""
import string
def check_pangram(text):
	res = sorted([i for i in text.lower() if i not in  string.punctuation])
	res = [i for i in res if i != ' ']
	new_l = []
	for i in res:
		if i not in new_l:
			new_l.append(i)
	if new_l == list(string.ascii_lowercase):
		return True
	else:
		return False
	#return 
a = check_pangram('Do big jackdaws love my sphinx of quartz?')
print(a)


		
