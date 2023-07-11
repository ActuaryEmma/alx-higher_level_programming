#!/usr/bin/python3
"""
module json used to convert an Object to a text file using JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file"""
    try:
        with open(filename, "w") as f:
            json_str = json.dumps(my_obj)
            f.write(json_str)
    except TypeError:
        print("[TypeError] {} is not JSON serializable".format(my_obj))
