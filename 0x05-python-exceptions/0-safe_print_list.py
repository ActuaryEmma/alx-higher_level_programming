#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if my_list:
        for x in my_list:
            try:
                print("{:d}".format(x))
            except SyntaxError:
                print("Error")
