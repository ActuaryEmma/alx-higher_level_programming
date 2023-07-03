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
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

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
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        return (self.__height) * (self.__width)

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """ print # """
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle = ""
        for row in range(self.height):
            for col in range(self.width):
                rectangle += "#"
            if row is not self.__height - 1:
                rectangle += "\n"
        return rectangle

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.__width, self.__height))
