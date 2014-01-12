#!/usr/bin/env python
from __future__ import print_function

import sys

# MAYBE DONE
# [4150, 4151, 54748, 92727, 93084, 194979]
# Sum: 443839

def power_sum(num, power):
	s = str(num)

	sum = 0
	for i in s:
		sum += (int(i) ** power)

	return sum


def main():

	print("1634 = %d" % power_sum(1634, 4))
	print("8208 = %d" % power_sum(8208, 4))
	print("9474 = %d" % power_sum(9474, 4))

	l = []
	for i in xrange(2, 1000000):
		if i == power_sum(i, 5):
			l.append(i)

	print(l)
	print("Sum: %d" % sum(l))





main()