#!/usr/bin/python3
def print_last_digit(number):
	last_digit = 0	
	if (number < 0):
		num = -number
		last_digit = num % 10
	else:
		last_digit = number % 10
	print(f"{last_digit}", end="")
	return last_digit
