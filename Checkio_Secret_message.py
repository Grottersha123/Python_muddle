"""
"Где умный человек прячет лист? В лесу. Но что если леса нет? ... Он выращивает лес и прячет его там."
-- Гилберт Кит Честертон

Когда-нибудь пробовали отправить секретное сообщение кому-то не пользуясь услугами почты? Вы можете использовать газету, чтобы рассказать кому-то свой секрет. Даже если кто-то найдет ваше сообщение, легко отмахнуться и сказать что это паранойя и теория заговора. Один из самых простых способов спрятать ваше секретное сообщение это использовать заглавные буквы. Давайте найдем несколько таких секретных сообщений.

Дан кусок текста. Соберите все заглавные буквы в одно слово в том порядке как они встречаются в куске текста.

Например: текст = "How are you? Eh, ok. Low or Lower? Ohhh.", если мы соберем все заглавные буквы, то получим сообщение "HELLO".

Входные данные: Текст как строка (юникод).

Выходные данные: Секретное сообщение как строка или пустая строка.

Пример:

find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO"
find_message("hello world!") == ""
    

Как это используется: Это простое упражнение по работе со строками: итерация, чтение и объединение.

Предусловие: 0 < len(text) ≤ 1000
all(ch in string.printable for ch in text)


"""
Big = 'ABCDEFGHIJKLMNOPQRSTVWXYZ'
def find_message(message):
	secrect = ''
	for i in message:
		if i in Big:
			secrect += i
	return secrect

a = find_message("how are you? eh, ok. low or lower? ohhh.")

print (a)