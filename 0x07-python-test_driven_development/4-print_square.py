#!/usr/bin/python3
"""
no module imported
"""


def print_square(size):
    """
    prints square of #
    """
    if type(size) is not int and type(size) is not float:
        raise TypeError("size must be an integer")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
