#!/usr/bin/python3
"""
no module
"""
import json


class Base():
    """class base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """return Json string representation"""
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)
