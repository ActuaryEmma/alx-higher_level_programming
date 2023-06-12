#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    total = []
    for i in range(2):
        if i < len_a:
            val_a = tuple_a[i]
        else:
            val_a = 0
        if i < len_b:
            val_b = tuple_b[i]
        else:
            val_b = 0
        total.append(val_a + val_b)
    return tuple(total)
