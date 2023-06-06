#!/usr/bin/python3
def print_last_digit(number):
	last_digit = 0	
	if (number < 0):
		num = -number
		last_digit = num % 10
	return last_digit
