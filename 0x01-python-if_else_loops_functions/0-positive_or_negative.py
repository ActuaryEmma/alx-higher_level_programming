#!/usr/bin/python3
import random
number = random.randint(-10, 10)  # return a random int within the range
if (number > 0):
    print(f"{number} is positive")
elif (number == 0):
    print(f"{number} is zero")
elif (number < 0):
    print(f"{number} is negative")
