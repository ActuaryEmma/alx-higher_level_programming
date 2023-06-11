#!/usr/bin/python3
import dis
def magic_calculation(a, b):
    return (a + (98 ** b))
print(dis.dis(magic_calculation))
