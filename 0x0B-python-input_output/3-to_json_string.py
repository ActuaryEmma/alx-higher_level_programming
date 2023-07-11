#!/usr/bin/python3
"""
module json used to convert the python dict to json string
"""
import json


def to_json_string(my_obj):
    """function that returns JSON representation of an object (string)"""
    json_data = json.dumps(my_obj)
    return json_data
