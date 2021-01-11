#!/usr/bin/python3


"""
2. Say my name
A function that prints My name is <first name> <last name>
say_my_name(first_name, last_name)
"""

def say_my_name(first_name, last_name=""):
    """
    Function that prints a name
    """
    if not type(first_name) is str:
        raise TypeError("first_name must be a string")
    if not type(last_name) is str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))