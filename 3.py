#!/usr/bin/env python
# Python 3 required
import locale
import sys
import math
import timeit

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

PRIMES = [2, 3, 5, 7,  11,  13,  17,  19,  23,  29, 
	31,  37,  41,  43,  47,  53,  59,  61,  67,  71, 
	73,  79,  83,  89,  97, 101, 103, 107, 109, 113, 
	127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 
	179, 181, 191, 193, 197, 199]

def is_prime(num):
	for i in PRIMES:
		if i >= num:
			break

		if num % i == 0:
			#print ("%d is divisible by %d" % (num, i))
			return False

	for i in range(PRIMES[-1], int(math.sqrt(num)), 2):
		if num % i == 0:
			return False

	return True

def is_prime2(num):
	k = 3
	while k*k <= num:
		if num % k == 0:
			return False
		k += 2
	return True

def main():
	num = int(sys.argv[1])
	print("Factoring %s" % locale.format("%d", num, grouping=True))	
	
	if num % 2 == 0:
		prime_factors = [2]
	else:
		prime_factors = []

	pager = 0
	for i in range(3, num, 2):
		if num % i == 0:
			print ("Factor: %s" % locale.format("%d", i, grouping=True))
			if is_prime2(i):
				prime_factors.append(i)
				print ("Prime Factor: %s" % locale.format("%d", i, grouping=True))

		# if pager % 1000000 == 0:
		# 	print("%.2f%%" % ((i / num) * 100))
		# 	pager = 0

		# pager += 1

	print("Prime Factors for %s" % locale.format("%d", num, grouping=True))
	print(prime_factors)


main()	