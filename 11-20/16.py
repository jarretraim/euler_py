#!/usr/bin/env python
from __future__ import print_function

import sys

# DONE? (1366)

def main():
	power = int(sys.argv[1])
	
	string = str(2**power)
	print(string)

	sum = 0
	for i in xrange(0, len(string)):
		sum += int(string[i])

	print("Sum: %d" % sum)



main()