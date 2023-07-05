#!/usr/bin/python3
"""
no module imported
"""


def add_integer(a, b=98):
    """
    add_integer - add two values a and b
    a is the first value and b the second value
    return the sum of a and b
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return (a + b)
