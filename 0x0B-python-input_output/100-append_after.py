#!/usr/bin/python3
'''Append after function'''


def append_after(filename="", search_string="", new_string=""):
    '''
    Inserts a line of text to a file
    After each line containing a specific string
    '''
    with open(filename, "r") as my_file:
        lines = my_file.readlines()
    with open(filename, "w") as new_file:
        for line in lines:
            if search_string in line:
                new_file.write(line + new_string)
            else:
                new_file.write(line)
