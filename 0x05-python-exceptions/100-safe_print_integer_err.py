#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except Exception as e:
        print("Exception: {0}".format(e), file=sys.stder)
        return False
    return True
