#!/usr/bin/env python
import locale

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

TOP = 20

def check_divisible(num):
	for i in range(2, TOP):
		if num % i != 0:
			return False

	return True


def main():

	current = TOP
	pager = 0

	while True:
		if (check_divisible(current)):
			print ("Smallest %d" % current)
			break
		else:
			current += TOP

		if pager % 1000 == 0:
			print("Currently checking: %d" % current)
			pager = 0

		pager += 1


main()