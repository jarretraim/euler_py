#!/usr/bin/env python
import locale

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

sum = 0

first = 1
second = 2

print(first)
print(second)

while True: 	
	third = first + second
	#print "(%i) %i + %i = %i" % (sum, first, second, third)

	first = second
	second = third

	output = locale.format("%d", second, grouping=True)

	if second % 2 == 0:
		output += "*"
		sum += second

	if second > 4000000:
		break

	print(output)

print(sum + 2)		# include the first term