#!/usr/bin/env python3
def uppercase(str):
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            aux = chr(ord(c) - 32)
        else:
            aux = c
        print("{}".format(aux), end="")
    print("")
