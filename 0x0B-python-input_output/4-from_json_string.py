#!/usr/bin/python3
import json
'''From jason string function'''


def from_json_string(my_str):
    '''Returns an object represented by a JSON string'''
    return json.loads(my_str)
