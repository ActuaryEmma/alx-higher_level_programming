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
    def width(self, width):
        """setter method"""
        self.__width = width

    @property
    def height(self):
        """getter method"""
        return self.__height

    @height.setter
    def height(self, height):
        """setter method"""
        self.__height = height

    @property
    def x(self):
        """getter method"""
        return self.__x

    @x.setter
    def x(self, x):
        """setter method"""
        self.__x = x

    @property
    def y(self):
        """getter method"""
        return self.y

    @y.setter
    def y(self, y):
        """setter method"""
        self.__y = y
