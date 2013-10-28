#!/usr/bin/env python

# Python 3 required

NATURALS = 100

def sum_squares():
	sum = 0
	for i in range(1, NATURALS+1):
		sum += i**2

	return sum

def square_sums():
	sum = 0
	for i in range(1, NATURALS+1):
		sum += i

	return sum**2


def main():
	sum_sq = sum_squares()
	sq_sum = square_sums()

	print ("%d - %d = %d" % (sq_sum, sum_sq, (sq_sum - sum_sq)))



main()