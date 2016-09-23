def sum_digits(number):
	b = 1
    num_str = str(number)
	for i in num_str:
		if i != '0':
			b *= int(i)
	return b
sum_digits(123) 