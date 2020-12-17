#!/usr/bin/python3
def best_score(a_dictionary):
    best = 0
    if a_dictionary:
        for i, j in a_dictionary.items():
            if j > best:
                best = j
                key = i
        return key
    return None
