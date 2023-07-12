#!/usr/bin/python3
"""
no module imported
"""


class Student():
    def __init__(self, first_name, last_name, age):
        """instantiate public attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if (attrs is None):
            return self.__dict__
        dic = {}
        for key, value in self.__dict__.items():
            for i in attrs:
                if key == i:
                    dic[key] = value
        return dic

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for i, j in json.items():
            self.__dict__[i] = j
