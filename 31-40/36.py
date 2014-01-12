#!/usr/bin/env python
from __future__ import print_function


# DONE
# SUM IS: 872187


MAX = 1000000


def is_palindrome(str_num):
	for i in range(0, len(str_num)-1):
		if str_num[i] != str_num[len(str_num)-i-1]:
			return False

	return True




def main():

	palindromes = []

	for i in range(1, MAX):
		if i % 100000 == 0:
			print ("Processing: {0}".format(i))

		if is_palindrome(str(i)) and is_palindrome("{0:b}".format(i)):
			palindromes.append(i)
			#print("{0} & {0:b}".format(i))


	print("Number of palindromes: {0}".format(len(palindromes)))
	print("Sum of list: {0}".format(sum(palindromes)))




main()
