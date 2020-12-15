#!/usr/bin/python3
def no_c(my_string):
    new = ""
    for i in range(0, len(my_string)):
        if my_string[i] == "C" or my_string[i] == "c":
            continue
        new = new + my_string[i]
    return(new)
