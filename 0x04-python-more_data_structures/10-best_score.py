#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max_value = None
    max_key = None
    for i, j in a_dictionary.items():
        if max_value is None or j > max_value:
            max_value = j
            max_key = i
    return max_key
