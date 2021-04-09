#!/usr/bin/python3
"""
Takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import requests
from sys import argv

if __name__ == '__main__':
    usr = argv[1]
    pwd = argv[2]
    r = requests.get('https://api.github.com/user', auth=(usr, pwd))
    r_json = r.json()
    print(r_json.get('id'))
