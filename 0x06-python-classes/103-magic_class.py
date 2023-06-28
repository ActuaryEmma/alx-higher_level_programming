#!/usr/bin/python3
import math
"""
math module has fuction pi
Write the Python class MagicClass that does
exactly the same as the following Python bytecode
"""


class MagicClass:
    """
    A class that represents a magic circle.

    Methods:
    - __init__(self, radius): Initializes MagicClass instance with a radius.
    - area(self): Calculates the area of the magic circle.
    - circumference(self): Calculates the circumference of the magic circle.
    """
    def __init__(self, radius):
        """
        Initialize the MagicClass instance.

        Parameters:
        - radius (int or float): The radius of the magic circle.

        Raises:
        - TypeError: If the radius is not a number.
        """
        self._MagicClass__radius = 0
        if type(radius) is not int or type(radius) is not float:
            raise TypeError("radius must be a number")
        else:
            self._MagicClass__radius = radius

    def area(self):
        """
        Calculate the area of the magic circle.

        Returns:
        - float: The area of the magic circle.
        """
        return self._MagicClass__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculate the circumference of the magic circle.

        Returns:
        - float: The circumference of the magic circle.
        """
        return 2 * math.pi * self._MagicClass__radius
