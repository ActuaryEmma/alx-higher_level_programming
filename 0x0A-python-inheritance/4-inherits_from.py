#!/usr/bin/python3
"""
no module used
"""


def inherits_from(obj, a_class):
    """
    returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class ; otherwise False.
    """
    if type(obj) is a_class:
        return False

    for base_class in type(obj).__bases__:
        if base_class is a_class or inherits_from(base_class, a_class):
            return True

    return False
