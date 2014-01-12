#!/usr/bin/env python
from __future__ import print_function

import sys

# DONE?
# First fib term with 1000 is f(4782)

DIGITS = 1000

def main():

	first = 1
	second = 1
	i = 3

	while True:
		third = first + second
		first = second
		second = third

		#print("f(%d) = %d" % (i, second))		

		if len(str(second)) == DIGITS:
			print("First fib term with %d is f(%d) = %d" % (DIGITS, i, second))
			break

		i += 1

main()