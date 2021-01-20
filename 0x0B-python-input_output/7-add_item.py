#!/usr/bin/python3

'''A script that adds all arguments to a Python list, and then save them to a file'''

from sys import argv
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if os.path.isfile('add_item.json'):
    p_list = load_from_json_file('add_item.json')
else:
    p_list = []
    
for arg in argv[1:]:
    p_list.append(arg)

save_to_json_file(p_list, 'add_item.json')
