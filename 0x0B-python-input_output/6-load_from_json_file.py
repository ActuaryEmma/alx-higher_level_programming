#!/usr/bin/python3
"""
used json module to convert JSON string to Object
"""
import json


def load_from_json_file(filename):
    """convert JSON string to object"""
    with open(filename) as f:
        json.load(f)
