#!/usr/bin/python3
'''Save to jason file function'''
import json


def save_to_json_file(my_obj, filename):
    '''Writes an Object to a text file, using a JSON representation'''
    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))
