#!/usr/bin/env python
from __future__ import print_function

import sys

# DONE (525)
# This is wrong.

def terms_in_chain(start):
	terms = 1
	
	while start != 1:
		if start % 2 == 0:
			start = start / 2
		else:
			start = (3 * start) + 1

		terms += 1

	return terms

def main():
	top = int(sys.argv[1])

	max = 0
	for i in xrange(1, top):
		terms = terms_in_chain(i)
		
		if terms > max:
			max = terms
			print("New Max: (%d -> %d)" % (i, max))

	print ("Local Max: %d" % max)

main()
