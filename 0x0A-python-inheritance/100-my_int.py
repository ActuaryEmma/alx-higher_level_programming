#!/usr/bin/python3
"""
no module
"""


class MyInt(int):
    """ class MyInt that inherits from int"""

    def __eq__(self, other):
        """
        Overrides the == operator.
        Args:
            other (int): The value to compare with.
        Returns:
            bool: True if the values are not equal, False otherwise.
        """
        return int(self) != other

    def __ne__(self, other):
        """
        Overrides the != operator.
        Args:
            other (int): The value to compare with.
        Returns:
            bool: True if the values are equal, False otherwise.
        """
        return int(self) == other
