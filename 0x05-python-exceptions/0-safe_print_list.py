#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if my_list:
        count = 0
        try:
            for i in range(x):
                print("{}".format(my_list[i]), end="")
                count += 1
        except (TypeError, IndexError):
            pass
    print()
    return (count)
