#!/usr/bin/python3


def inherits_from(obj, a_class):
    if type(obj) is a_class:
        return False
    elif isinstance(obj, a_class):
        return True
    else:
        return False
