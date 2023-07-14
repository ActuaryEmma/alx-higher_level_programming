#!/usr/bin/python3
"""
no module
"""
from models.base import Base


class Rectangle(Base):
    """ class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize the attributes"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """getter method"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter method"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter method"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter method"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter method"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter method"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if not bool(value):
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter method"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter method"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if not bool(value):
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """return area of the rectangle"""
        return self.__height * self.__width

    def display(self):
        """print #"""
        for row in range(self.height):
            for col in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """returns a string"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                        self.__x,
                                                        self.__y,
                                                        self.__width,
                                                        self.__height))
