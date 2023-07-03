#!/usr/bin/python3
"""
no module used
"""


class Rectangle:
    """
    A class that represents a Rectangle.
    """
    def __init__(self, width=0, height=0):
        """
        Initialize width and height
        """
        if type(width) is not int:
            return TypeError("width must be an integer")
        if width < 0:
            return ValueError("width must be >= 0")
        if type(height) is not int:
            return TypeError("width must be an integer")
        if height < 0:
            return ValueError("width must be >= 0")

        self.__height = height
        self.__width = width

    @property
    def width(self):
        """ getter"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """setter"""
        if type(value) is not int:
            return TypeError("width must be an integer")
        if value < 0:
            return ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """setter"""
        if type(value) is not int:
            return TypeError("height must be an integer")
        if value < 0:
            return ValueError("height must be >= 0")
        self.__height = value
