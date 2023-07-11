#!/usr/bin/python3
"""
no module
"""


def add_attribute(obj, attr, value):
    """function that adds a new attribute"""
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
    if not hasattr(obj, attr):
        raise TypeError("can't add new attribute")
