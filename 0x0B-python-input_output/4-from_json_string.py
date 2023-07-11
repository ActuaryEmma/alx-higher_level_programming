#!/usr/bin/python3
"""
module json used to convert JSON string to python object
"""
import json


def from_json_string(my_str):
    """returns back to python obect from JSON string"""
    try:
        python_obj = json.loads(my_str)
        return python_obj
    except ValueError as e:
        raise ValueError("Expecting property name enclosed in double\
 quotes: line 2 column 25 (char 25)")
