#!/usr/bin/python3
"""
inherit the Rectangle class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square inherit from class Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """class constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """return string representation of an object"""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.height)
