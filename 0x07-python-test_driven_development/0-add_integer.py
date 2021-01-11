#!/usr/bin/python3

"""
0. Integers addition
A function that adds 2 integers
add_integer(a, b)
"""


def add_integer(a, b=98):
    """
    Function that add two integers
    """
    if not type(a) is int and not type(a) is float:
        raise TypeError("a must be an integer")
    if not type(b) is int and not type(b) is float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
