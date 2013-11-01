#!/usr/bin/env python
from __future__ import print_function

import sys
import math

# DONE? (648)

def main():
	n = int(sys.argv[1])

	factorial = math.factorial(n)

	s_factorial = str(factorial)
	sum = 0
	for i in xrange(0, len(s_factorial)):
		sum += int(s_factorial[i])

	print(sum)



main()