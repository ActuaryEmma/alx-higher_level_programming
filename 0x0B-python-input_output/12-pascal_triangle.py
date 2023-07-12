#!/usr/bin/python3
"""no module"""


if __name__ == "__main__":
    """executed if its the main function"""
    def pascal_triangle(n):
        """return list of lists of integers"""

        list1 = []
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                list1.append(j)
        return list1
