#!/usr/bin/env python
from __future__ import print_function

import sys

# NOT DONE

# Brute force is too slow
# Number of factors is not consistently increasing, so the binary search didn't work

def num_factors(triangle):
	s = sum(xrange(1,triangle+1))	

	factors = 0
	for i in xrange(1, s):
		if s % i == 0:
			factors += 1
	return factors

def binary_search(target):
	low = 1
	high = 100

	while True:		
		mid = int((high+low) / 2)
		print("High: %d, Mid: %d, Low: %d" % (high, mid, low))

		num_fac = num_factors(mid)
		print("Factoring triangle number %d yields %d factors." % (mid, num_fac))

		if num_fac < target:
			low = mid			
		elif num_fac > target:
			high = mid
		else:
			print("Found %d factors for triangle of %d" % (num_fac, mid))
			break


	print("Checking for minimum.")
	i = 1
	while num_fac == target:
		num_fac = num_factors(mid - i)
		print("Triangle number %d has %d factors." % ((mid - i), num_fac))
		i += 1

	print("Minimum triangle number with %d factors is %d" % (num_fac, (mid - i)))

def main():
	target = int(sys.argv[1])
	print("Looking for %d factors." % target)
	

	



main()