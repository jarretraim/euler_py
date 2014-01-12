#!/usr/bin/env python
from __future__ import print_function

import sys

# DONE? 
# Number of distinct items: 9183

MIN_A = 2
MAX_A = 100

MIN_B = 2
MAX_B = 100


def main():

	s = set()

	for i in xrange(MIN_A, MAX_A+1):
		for j in xrange(MIN_B, MAX_B+1):
			#print ("%d ^ %d = %d" % (i, j, (i**j)))
			s.add(i**j)

	#print(sorted(s))
	print ("Number of distinct items: %d" % len(s))



main()