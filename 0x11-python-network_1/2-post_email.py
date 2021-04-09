#!/usr/bin/python3
''' '''
import urllib.request
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]

    value = {'email': email}
    data = urllib.parse.urlencode(value)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
