#!/usr/bin/env python
import locale

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

DIGITS = 3

def is_palindrome(num):
	str_num = str(num)

	for i in range(0, int(len(str_num)/2)):
		if str_num[i] != str_num[len(str_num)-(i+1)]:
			#print (str_num[i])
			#print (str_num[len(str_num)-(i+1)])
			return False

	return True



def main():
	counter = 0

	palindromes = []

	for i in range(10**(DIGITS-1), (10**DIGITS), 1):
		for j in range(10**(DIGITS-1), (10**DIGITS), 1):
			counter += 1

			t = i*j
			if is_palindrome(t):
				palindromes.append(t)

			#print("%d (%d, %d): %d -> %s" % (counter, i, j, t, str(is_palindrome(t))))			

	print("Completed checking %d possibilities." % counter)
	print(sorted(palindromes)[len(palindromes)-1])


main()
#print(is_palindrome(9110))
#print(is_palindrome(9119))
#print(is_palindrome(7056))