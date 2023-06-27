#!/usr/bin/python3
"""
class square with private instance size and
size must be an int else raise an error
"""


class Square:
    """Represents a Sqaure with a size"""
    def __init__(self, size=0):
        """Initialize the size"""
        try:
            self.__size = size
        except TypeError:
            raise TypeError("size must be an integer")
        except ValueError:
            raise ValueError("size must be >= 0")
