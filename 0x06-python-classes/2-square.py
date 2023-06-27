#!/usr/bin/python3
"""
class square with private instance size and
size must be an int else raise an error
"""


class Square:
    """Represents a Sqaure with a size"""
    def __init__(self, size=0):
        """Initialize the size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
