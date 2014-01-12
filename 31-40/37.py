#!/usr/bin/env python

# DONE
# SUM IS 748317


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

def is_truncatable(num):
	if trunc_left(num) and trunc_right(num):
		return True


def trunc_right(num):
	s = str(num)

	for i in range(1, len(s)):
		print("Checking right trunc of {0}: {1}".format(num, s[:i]))
		if not is_prime(int(s[:i])):
			return False

	return True


def trunc_left(num):
	s = str(num)

	for i in range(1, len(s)):
		print("Checking left trunc of {0}: {1}".format(num, s[i:]))
		if not is_prime(int(s[i:])):
			return False

	return True

def main():

	truncs = []
	i = 9

	print("3797 is prime: {0}".format(is_prime(3797)))
	print("3797 truncs left: {0}".format(trunc_left(3797)))
	print("3797 truncs right: {0}".format(trunc_right(3797)))

	print("29 is prime: {0}".format(is_prime(29)))
	print("29 truncs left: {0}".format(trunc_left(29)))
	print("29 truncs right: {0}".format(trunc_right(29)))

	print("43 is prime: {0}".format(is_prime(43)))
	print("43 truncs left: {0}".format(trunc_left(43)))
	print("43 truncs right: {0}".format(trunc_right(43)))

	while len(truncs) < 11:
		while not is_prime(i):
			i += 2

		#print("Trying prime: {0}".format(i))
		if is_truncatable(i):
			truncs.append(i)
			print("Found {0} truncatable primes so far.".format(len(truncs)))

		i += 2


	print ("Truncable Primes: {0}".format(truncs))
	print("Sum of truncatable primes: {0}".format(sum(truncs)))





main()
