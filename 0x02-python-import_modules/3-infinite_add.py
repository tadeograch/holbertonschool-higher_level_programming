#!/usr/bin/python3
import sys
if __name__ == "__main__":
    a = 0
    if len(sys.argv) != 1:
        for i in range(1, len(sys.argv)):
            a += int(sys.argv[i])
    print("{:d}".format(a))
