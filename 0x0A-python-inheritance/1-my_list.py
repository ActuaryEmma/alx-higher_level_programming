#!/usr/bin/python3
"""
no module used
"""


class MyList(list):
    """ class that inherits from list """
    def print_sorted(self):
        """function that sort the list in ascending order"""
        print(self)
        sorted_list = sorted(self)
        print(sorted_list)
