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
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def integer_validator(self, name, value):
        """checks for errors"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be > 0")

    def integer_validator2(self, name, value):
        """checks for errors"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value < 0:
            raise ValueError(f"{name} must be >= 0")

    @property
    def width(self):
        """getter method"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter method"""
        self.integer_validator("width", value)
        self.__width = value

    @property
    def height(self):
        """getter method"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter method"""
        self.integer_validator("height", value)
        self.__height = value

    @property
    def x(self):
        """getter method"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter method"""
        self.integer_validator2("x", value)
        self.__x = value

    @property
    def y(self):
        """getter method"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter method"""
        self.integer_validator2("y", value)
        self.__y = value

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

    def update(self, *args, **kwargs):
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
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.__width = value
                elif key == "height":
                    self.__heigth = value
                elif key == "x":
                    self.__x = value
                elif key == "y":
                    self.__y = value

    def to_dictionary(self):
        """return dictionary representation of a Rectangle"""
        class_dict = {'x': self._Rectangle__x,
                      'y': self._Rectangle__y,
                      'id': self.id,
                      'height': self._Rectangle__height,
                      'width': self._Rectangle__width}
        return class_dict
