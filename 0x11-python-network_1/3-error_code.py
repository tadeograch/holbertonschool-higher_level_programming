#!/usr/bin/python3
'''
Takes in a URL, sends a request to the URL
and displays the body of the response
(decoded in utf-8).
'''
import urllib.request
from sys import argv

if __name__ == "__main__":
    try:
        req = urllib.request.Request(argv[1])
        with urllib.request.urlopen(req) as response:
            the_page = response.read()
            print(the_page.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
