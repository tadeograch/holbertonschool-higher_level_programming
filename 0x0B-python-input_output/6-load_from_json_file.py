#!/usr/bin/python3
import json
'''Load from json file function'''


def load_from_json_file(filename):
    '''Creates an Object from a “JSON file”'''
    with open(filename, "r") as f:
        return json.load(f)
