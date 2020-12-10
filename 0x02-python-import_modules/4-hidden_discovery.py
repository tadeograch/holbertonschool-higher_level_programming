#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    list = dir(hidden_4)
    len = len(list)
    str = "__"
    for i in range(0, len):
        if list[i][:2] != str:
            print("{}".format(list[i]))
