#!/usr/bin/python3
import json
'''Save to jason file function'''


def save_to_json_file(my_obj, filename):
    '''Writes an Object to a text file, using a JSON representation'''
    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))
