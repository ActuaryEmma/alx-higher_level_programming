#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
module BaseGeomety is the parent class
"""


class Rectangle(BaseGeometry):
    """ class Rectangle that inherits from BaseGoemetry """
    def __init__(self, width, height):
        """instantiate width and height"""
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
