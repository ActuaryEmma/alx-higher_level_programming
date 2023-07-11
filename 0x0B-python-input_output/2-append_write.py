#!/usr/bin/python3
"""
no module
"""


def append_write(filename="", text=""):
    """function that appends a string at end of a file"""
    with open(filename, "a", encoding="utf-8") as f:
        append_text = f.write(text)
    return append_text
