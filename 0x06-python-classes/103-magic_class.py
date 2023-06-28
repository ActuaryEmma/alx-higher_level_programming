#!/usr/bin/python3
"""
math module has fuction pi
Write the Python class MagicClass that does
exactly the same as the following Python bytecode
"""
import math


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
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        Calculate the area of the magic circle.

        Returns:
        - float: The area of the magic circle.
        """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """
        Calculate the circumference of the magic circle.

        Returns:
        - float: The circumference of the magic circle.
        """
        return (2 * math.pi) * self.__radius
