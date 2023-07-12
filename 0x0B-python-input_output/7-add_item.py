#!/usr/bin/python3
from sys import argv
from json import JSONDecodeError
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

list1 = []
try:
    list1 = list(load_from_json_file("add_item.json"))
except FileNotFoundError:
    pass

for arg in range(1, len(argv)):
    list1.append(argv[arg])

save_to_json_file(list1, "add_item.json")
