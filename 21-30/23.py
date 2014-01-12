#!/usr/bin/env python
from __future__ import print_function

import sys

# DONE?
# Sum of 24632 numbers that cannot be expressed as the sum of two abundant numbers: 346398923


def is_perfect(num):
	return sum(divisors(num)) == num

def is_abundant(num):
	return sum(divisors(num)) > num

def is_deficient(num):
	return sum(divisors(num)) < num


def divisors(num):
	divs = []
	for i in range(1, int(num/2)+1):
		if num % i == 0:
			divs.append(i)

	#print("%d = %s" % (num, divs))
	return divs


def factor(num):
	factors = set()

	i = 2
	while i < num:
		if num % i == 0:
			factors.add(i)
			factors.add(num / i)
			num = num / i
			factors = set.union(factors, factor(num))

		i += 1

	return factors

def is_sum_of_abundant(num):
	factors = factor(num)

	for i in factors:
		if i < 12:
			continue

		if is_abundant(i):
			for j in factors:
				if j < 12:
					continue

				if i + j == num:
					#print("%d + %d = %d" % (i, j, num))
					return True

	return False



def main():
	print("Is 12 perfect   -> %s" % is_perfect(12))
	print("Is 12 abundant  -> %s" % is_abundant(12))
	print("Is 12 deficient -> %s" % is_deficient(12))


	print("Is 24 sum of abundant -> %s" % is_sum_of_abundant(24))
	print("Is 25 sum of abundant -> %s" % is_sum_of_abundant(25))
	print("Is 20 sum of abundant -> %s" % is_sum_of_abundant(20))

	no_abundant_sums = []
	for i in xrange(1, 28123):
		if not is_sum_of_abundant(i):
			no_abundant_sums.append(i)

	#print(no_abundant_sums)

	print("Sum of %d numbers that cannot be expressed as the sum of two abundant numbers: %d" % 
		 (len(no_abundant_sums), sum(no_abundant_sums)))







main()