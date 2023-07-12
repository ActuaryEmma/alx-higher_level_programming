#!/usr/bin/python3
"""
used json module to convert JSON string to Object
"""
import json


def load_from_json_file(filename):
    """convert JSON string to object"""
    try:
        with open(filename) as f:
            new_obj = json.load(f)
    except ValueError:
        new_obj = None
    return new_obj
