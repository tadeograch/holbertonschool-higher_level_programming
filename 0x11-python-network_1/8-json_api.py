#!/usr/bin/python3
'''
Takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user
with the letter as a parameter.
'''
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) == 2:
        q = argv[1]
    else:
        q = ""
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        r_dict = r.json()
        r_id = r_dict.get('id')
        r_name = r_dict.get('name')
        if len(r_dict) == 0 or not r_id or not r_name:
            print("No result")
        else:
            print("[{}] {}".format(r_dict.get('id'), r_dict.get('name')))
    except:
        print("Not a valid JSON")
