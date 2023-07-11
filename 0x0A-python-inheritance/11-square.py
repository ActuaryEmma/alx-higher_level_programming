#!/usr/bin/python3
"""
module Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class Rectangle """

    def __init__(self, size):
        """ instantiate size"""
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ area of a square"""

        return self.__size * self.__size

    def __str__(self):
        """print"""

        return (f"[Square] {self.__size}/{self.__size}")
