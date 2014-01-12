#!/usr/bin/env python
from __future__ import print_function

import sys

# WRONG
# Sum of 15 amicable numbers: 40284


def is_amicable(num):
	da = sum(divisors(num))
	#print("d(%d) = %d" % (num, da))

	db = sum(divisors(da))
	#print("d(%d) = %d" % (da, db))

	if num == db:
		print("d(%d) = %d and d(%d) == %d." % (num, da, da, db))
		return True
	else: 
		return False




def divisors(num):
	divs = []
	for i in range(1, int(num/2)+1):
		if num % i == 0:
			divs.append(i)

	return divs


def main():

	amicable = []
	for i in range(0, 10000):
		if is_amicable(i):
			amicable.append(i)

	print("Sum of %d amicable numbers: %d" % (len(amicable), sum(amicable)))


main()

