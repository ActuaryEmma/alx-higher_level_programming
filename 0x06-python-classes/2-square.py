#!/usr/bin/python3
"""
class square with private instance size and
size must be an int else raise an error
"""


class Square:
    """Represents a Sqaure with a size"""
    try:
        def __init__(self, size=0):
            """Initialize the size"""
            self.__size = size
    except TypeError:
        print("size must be an integer")
    except ValueError:
        print("size must be >= 0")
