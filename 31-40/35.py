#!/usr/bin/env python
from __future__ import print_function


HIGH = 100

def is_prime(num):
	if num == 1:
		return False

	if num == 2:
		return True

	if num % 2 == 0:
		return False

	k = 3
	while k*k <= num:
		if num % k == 0:
			return False
		k += 2
	return True

def gen_rotations(num):
	rotations = [num]
	stnum = str(num)

	length = len(stnum)

	if length < 2:
		return rotations
	
	for i in xrange(0, length-1):
		end = stnum[length - 1]
		stnum = end + stnum[:length-1]
		rotations.append(int(stnum))

	print("Rotations for %d: %s" % (num, rotations))

	return rotations


def main():
	primes = set()

	for i in xrange(2, HIGH):
		rotations = gen_rotations(i)
		
		for j in rotations:
			if is_prime(j):
				primes.add(j)
				break

	print("Primes: %s" % str(primes))
	print("Prime Count: %d" % len(primes))



main()