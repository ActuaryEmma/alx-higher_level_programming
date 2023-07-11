#!/usr/bin/python3
"""
no module used
"""


def read_file(filename=""):
    """ function that reads and open a file"""
    with open(filename, encoding="utf-8") as f:
        print("{}".format(f.read()), end="")
