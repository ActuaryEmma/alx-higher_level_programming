#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)		
last_dig = abs(number) % 10

if (number < 0):
    last_dig  *= -1

tx = "Last digit of {number} is {last_dig} and is "

if (last_dig > 5):
    tx += "greater than 5"
elif (last_dig == 0):
    tx += "0"
else:
    tx += "less than 6 and not 0"

print(tx.format(number, last_dig))		
