#!/usr/bin/python3
'''Read file function'''


def read_file(filename=""):
    '''Reads a textfile and prints it to stdout'''
    with open(filename, "r") as f:
            print(f.read(), end="")
