#!/usr/bin/python3
"""
module json used to convert JSON string to python object
"""
import json


def from_json_string(my_str):
    """returns back to python obect from JSON string"""
    return json.loads(my_str)
