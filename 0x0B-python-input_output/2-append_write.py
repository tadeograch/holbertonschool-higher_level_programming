#!/usr/bin/python3
'''Append write function'''


def append_write(filename="", text=""):
    '''
    Appends a string at the end of a text file
    Returns the number of characters added
    '''
    c = len(text)
    with open(filename, "a") as f:
        f.write(text)
    return c
