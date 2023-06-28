#!/usr/bin/python3
"""
class that defines a square
private instance attribute : size
catch TypeError(only int) and ValueError(not less than 0)
getter : def size(self)
setter : def size(self, value)
public instance method: def area(self) that returns current square area
public instance method: def my_print(self):
that prints in stdout the square with the character #
if size is equal to 0, print an empty line
"""


class Square:
    """represent a sqaure with a size"""
    def __init__(self, size=0):
        """Initialize the size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """find area of a square"""
        return (self.__size) * (self.__size)

    def my_print(self):
        """prints in stdout the square with the character #"""
        row, col = 0, 0
        if self.__size == 0:
            print()
            return (None)
        for row in range(0, self.__size, 1):
            for col in range(0, self.__size, 1):
                print('#', end="")
            print()

    @property
    def size(self):
        """getter method: returns the size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter method: change the size to value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
