#!/usr/bin/python3
"""
no module
"""


def write_file(filename="", text=""):
    """function that open and write a string in file"""
    with open(filename, "w", encoding="utf-8") as f:
        written_text = f.write(text)
    return written_text
