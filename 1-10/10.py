#!/usr/bin/env python

# Python 3 required

def is_prime(num):
	k = 3
	while k*k <= num:
		if num % k == 0:
			return False
		k += 2
	return True

def main():

	sum = 2
	for i in range(3, 2000000, 2):
		if (is_prime(i)):
			print(sum)
			sum += i

	print("Total: %d" % sum)






main()	