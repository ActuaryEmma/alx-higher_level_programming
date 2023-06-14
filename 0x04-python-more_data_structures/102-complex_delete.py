#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys_to_delete = []
    for i, j in a_dictionary.items():
        if j == value:
            keys_to_delete.append(i)
    for key in keys_to_delete:
        del a_dictionary[key]
    return a_dictionary
