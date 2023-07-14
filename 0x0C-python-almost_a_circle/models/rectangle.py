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
        for _ in range(self.__y):
            print()
        for row in range(self.__height):
            for _ in range(self.__x):
                print(" ", end="")
            print("#" * self.__width)

    def __str__(self):
        """returns a string representation of object """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                        self.__x,
                                                        self.__y,
                                                        self.__width,
                                                        self.__height))

    def update(self, *args):
        """public method that assigns an argument to each attribute"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]
