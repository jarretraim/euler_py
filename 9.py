#!/usr/bin/env python

# Python 3 required

MAX = 1000


def variation():
	for n in range(1, 25):
		a = (2*n) + 1
		b = (2*n) * (n + 1)
		c = (2*n) * (n + 1) + 1


		print("%d^2 + %d^2 = %d^2 (%d)" % (a, b, c, (a+b+c)))

		a += 1

def euclid():
	for n in range(1, MAX):
		for m in range(n+1, MAX):
			a = (m**2) - (n**2)
			b = 2 * m * n
			c = (m**2) + (n**2)

			#print("%d^2 + %d^2 = %d^2 (%d)" % (a, b, c, (a+b+c)))

			if (a + b + c) == 1000:
				print("**** %d + %d + %d = 1000" % (a, b, c))
				print("Product: %d" % (a*b*c))
				break


def main():
	euclid()

main()