#!/usr/bin/python3
"""
class square that defines a square
have private instance attribute size that handle TypeError and ValueError
Public instance method: area that returns the current square area
"""


class Square:
    """class sqaure that find area of a square"""
    def __init__(self, size=0):
        """Initialize the size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """finding area of a sqaure"""
        return (self.__size) * (self.__size)
