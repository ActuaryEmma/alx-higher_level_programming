#!/usr/bin/python3
import math
"""
Write the Python class MagicClass that does
exactly the same as the following Python bytecode
"""


class MagicClass:
    """class MagicClass"""
    def __init__(self, radius):
        """initialize the radius"""
        self._MagicClass__radius = 0
        if type(radius) is not int or type(radius) is not float:
            raise TypeError("radius must be a number")
        else:
            self._MagicClass__radius = radius

    def area(self):
        """find the area"""
        return self._MagicClass__radius ** 2 * math.pi

    def circumference(self):
        """find the circumference"""
        return 2 * math.pi * self._MagicClass__radius
