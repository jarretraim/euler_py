#!/usr/bin/env python

# Python 3 required

PRIME = 10001

def is_prime(num):
	k = 3
	while k*k <= num:
		if num % k == 0:
			return False
		k += 2
	return True

def main():
	primes = [2]
	current = 3

	while True:
		if is_prime(current):
			primes.append(current)

			print("%d primes found. %d left to go" % 
				(len(primes), PRIME - len(primes)))

			if len(primes) == PRIME:
				print(primes[len(primes) - 1])
				break

		current += 2





main()