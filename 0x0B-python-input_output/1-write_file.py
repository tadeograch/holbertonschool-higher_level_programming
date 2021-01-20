#!/usr/bin/python3
'''Write file function'''


def write_file(filename="", text=""):
    '''
    Writes a string to a text file
    Returns the number of characters written
    '''
    c = len(text)
    with open(filename, "w") as f:
        f.write(text)
    return c
